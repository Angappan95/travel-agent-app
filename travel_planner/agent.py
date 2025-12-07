import datetime
from typing import Optional, Dict, List, Any
import json

from google.adk.agents import Agent
from flight_agent.agent import search_flights
from hotel_agent.agent import search_hotels
from activities_agent.agent import search_activities, get_activities_by_category
from config import MODEL_NAME

def create_comprehensive_travel_plan(
    source: str,
    destination: str,
    travel_date: Optional[str] = None,
    return_date: Optional[str] = None,
    budget: Optional[int] = None,
    travelers: int = 1,
    preferences: Optional[str] = None
) -> dict:
    """Creates a comprehensive travel plan including flights, hotels, and activities.

    Args:
        source (str): The departure city.
        destination (str): The destination city.
        travel_date (str, optional): The travel date in YYYY-MM-DD format. Defaults to today.
        return_date (str, optional): The return date in YYYY-MM-DD format. Defaults to next day.
        budget (int, optional): Total budget in rupees.
        travelers (int, optional): Number of travelers. Defaults to 1.
        preferences (str, optional): Travel preferences (e.g., "luxury", "budget", "adventure", "cultural").

    Returns:
        dict: Comprehensive travel plan with flights, hotels, and activities.
    """
    
    # Set default dates
    if not travel_date:
        travel_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if not return_date:
        travel_date_obj = datetime.datetime.strptime(travel_date, "%Y-%m-%d")
        return_date = (travel_date_obj + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
    
    # Calculate trip duration
    travel_date_obj = datetime.datetime.strptime(travel_date, "%Y-%m-%d")
    return_date_obj = datetime.datetime.strptime(return_date, "%Y-%m-%d")
    duration_days = (return_date_obj - travel_date_obj).days
    
    # Initialize the travel plan
    travel_plan = {
        "trip_overview": {
            "source": source.title(),
            "destination": destination.title(),
            "travel_date": travel_date,
            "return_date": return_date,
            "duration_days": duration_days,
            "travelers": travelers,
            "preferences": preferences,
            "budget": f"₹{budget:,}" if budget else "Not specified"
        },
        "status": "success",
        "plan_generated_at": datetime.datetime.now().isoformat()
    }
    
    # Search for flights
    outbound_flights = search_flights(source, destination, travel_date)
    return_flights = search_flights(destination, source, return_date)
    
    # Search for hotels
    hotel_filters = {}
    if budget and preferences:
        # Allocate budget: 40% flights, 40% hotels, 20% activities
        max_hotel_budget = int((budget * 0.4) / duration_days) if duration_days > 0 else None
        if max_hotel_budget:
            hotel_filters["max_price"] = max_hotel_budget
        
        if "luxury" in preferences.lower():
            hotel_filters["min_rating"] = 4
        elif "budget" in preferences.lower():
            hotel_filters["max_price"] = 5000
    
    hotels = search_hotels(
        destination, 
        travel_date, 
        return_date,
        **hotel_filters
    )
    
    # Search for activities
    activity_filters = {}
    if budget:
        # Allocate 20% of budget for activities
        max_activity_budget = int(budget * 0.2 / max(1, duration_days))
        activity_filters["max_price"] = max_activity_budget
    
    if preferences:
        if "adventure" in preferences.lower():
            activity_filters["category"] = "Adventure"
        elif "cultural" in preferences.lower() or "heritage" in preferences.lower():
            activity_filters["category"] = "Heritage"
        elif "food" in preferences.lower() or "culinary" in preferences.lower():
            activity_filters["category"] = "Culinary"
    
    activities = search_activities(destination, **activity_filters)
    
    # Build the comprehensive plan
    travel_plan["flights"] = {
        "outbound": outbound_flights,
        "return": return_flights
    }
    
    travel_plan["accommodation"] = hotels
    travel_plan["activities"] = activities
    
    # Calculate estimated costs
    total_cost_estimate = 0
    cost_breakdown = {}
    
    # Flight costs
    if outbound_flights["status"] == "success" and return_flights["status"] == "success":
        # Get cheapest flight options
        outbound_cost = min([int(f["price"].replace("₹", "").replace(",", "")) 
                           for f in outbound_flights["flights"]]) if outbound_flights["flights"] else 0
        return_cost = min([int(f["price"].replace("₹", "").replace(",", "")) 
                          for f in return_flights["flights"]]) if return_flights["flights"] else 0
        flight_cost = (outbound_cost + return_cost) * travelers
        cost_breakdown["flights"] = f"₹{flight_cost:,}"
        total_cost_estimate += flight_cost
    
    # Hotel costs
    if hotels["status"] == "success" and hotels["hotels"]:
        cheapest_hotel = min(hotels["hotels"], 
                           key=lambda h: int(h["price_per_night"].replace("₹", "").replace(",", "")))
        hotel_cost_per_night = int(cheapest_hotel["price_per_night"].replace("₹", "").replace(",", ""))
        hotel_total_cost = hotel_cost_per_night * duration_days
        cost_breakdown["accommodation"] = f"₹{hotel_total_cost:,} ({duration_days} nights)"
        total_cost_estimate += hotel_total_cost
    
    # Activity costs
    if activities["status"] == "success" and activities["activities"]:
        # Estimate 2-3 activities per day
        activities_per_day = 2
        total_activities = duration_days * activities_per_day
        avg_activity_cost = 0
        free_activities = [a for a in activities["activities"] if a["price"] == "₹free"]
        paid_activities = [a for a in activities["activities"] if a["price"] != "₹free"]
        
        if paid_activities:
            avg_activity_cost = sum([int(a["price"].replace("₹", "").replace(",", "")) 
                                   for a in paid_activities[:total_activities]]) // min(len(paid_activities), total_activities)
        
        activity_cost = avg_activity_cost * min(total_activities, len(paid_activities))
        cost_breakdown["activities"] = f"₹{activity_cost:,} (estimated {total_activities} activities)"
        total_cost_estimate += activity_cost
    
    travel_plan["cost_estimate"] = {
        "total": f"₹{total_cost_estimate:,}",
        "per_person": f"₹{total_cost_estimate // travelers:,}" if travelers > 1 else f"₹{total_cost_estimate:,}",
        "breakdown": cost_breakdown,
        "budget_status": "Within budget" if budget and total_cost_estimate <= budget else "Over budget" if budget else "No budget specified"
    }
    
    # Add recommendations
    recommendations = []
    
    if preferences:
        if "budget" in preferences.lower():
            recommendations.append("Consider booking hostels or budget hotels to save money")
            recommendations.append("Look for free activities and walking tours")
        elif "luxury" in preferences.lower():
            recommendations.append("Book premium hotels with spa and fine dining")
            recommendations.append("Consider private tours and premium experiences")
        
        if "adventure" in preferences.lower():
            recommendations.append("Pack appropriate gear for adventure activities")
            recommendations.append("Check weather conditions for outdoor activities")
        
        if "cultural" in preferences.lower():
            recommendations.append("Research local customs and traditions")
            recommendations.append("Visit museums and heritage sites early to avoid crowds")
    
    # General recommendations
    recommendations.extend([
        f"Book flights at least 2-3 weeks in advance for better prices",
        f"Consider travel insurance for {duration_days}-day trips",
        "Check visa requirements if traveling internationally",
        "Pack according to the destination's weather and cultural norms"
    ])
    
    travel_plan["recommendations"] = recommendations
    
    return travel_plan

def search_destination_activities(destination: str, activity_type: Optional[str] = None) -> dict:
    """Search for activities in a specific destination with optional type filtering.
    
    Args:
        destination (str): The destination city.
        activity_type (str, optional): Type of activity (Adventure, Heritage, Culinary, etc.).
        
    Returns:
        dict: Available activities in the destination.
    """
    if activity_type:
        return search_activities(destination, category=activity_type)
    else:
        return search_activities(destination)

def get_travel_inspiration(activity_category: str) -> dict:
    """Get travel inspiration based on activity preferences across all destinations.
    
    Args:
        activity_category (str): The type of activities you're interested in.
        
    Returns:
        dict: Cities and activities matching your interests.
    """
    return get_activities_by_category(activity_category)

def compare_destinations(destinations: List[str], preferences: Optional[str] = None) -> dict:
    """Compare multiple destinations based on available activities and accommodations.
    
    Args:
        destinations (List[str]): List of destination cities to compare.
        preferences (str, optional): Travel preferences to filter comparison.
        
    Returns:
        dict: Comparison of destinations with recommendations.
    """
    
    comparison = {
        "destinations_compared": destinations,
        "preferences": preferences,
        "comparison_results": {},
        "recommendation": None
    }
    
    for destination in destinations:
        dest_info = {
            "city": destination.title(),
            "hotels": search_hotels(destination),
            "activities": search_activities(destination)
        }
        
        # Add scoring based on preferences
        score = 0
        highlights = []
        
        if dest_info["hotels"]["status"] == "success":
            hotels = dest_info["hotels"]["hotels"]
            avg_hotel_price = sum([int(h["price_per_night"].replace("₹", "").replace(",", "")) 
                                 for h in hotels]) // len(hotels)
            luxury_hotels = len([h for h in hotels if h["rating"] >= 4])
            
            dest_info["hotel_summary"] = {
                "total_hotels": len(hotels),
                "avg_price": f"₹{avg_hotel_price:,}",
                "luxury_options": luxury_hotels
            }
            
            if preferences:
                if "budget" in preferences.lower() and avg_hotel_price <= 5000:
                    score += 2
                    highlights.append("Budget-friendly accommodation")
                elif "luxury" in preferences.lower() and luxury_hotels > 0:
                    score += 2
                    highlights.append("Luxury accommodation available")
        
        if dest_info["activities"]["status"] == "success":
            activities = dest_info["activities"]["activities"]
            activity_categories = set([a["category"] for a in activities])
            
            dest_info["activity_summary"] = {
                "total_activities": len(activities),
                "categories": list(activity_categories),
                "avg_rating": round(sum([a["rating"] for a in activities]) / len(activities), 1)
            }
            
            if preferences:
                if "adventure" in preferences.lower() and "Adventure" in activity_categories:
                    score += 3
                    highlights.append("Great for adventure activities")
                elif "cultural" in preferences.lower() and "Heritage" in activity_categories:
                    score += 3
                    highlights.append("Rich cultural experiences")
                elif "food" in preferences.lower() and "Culinary" in activity_categories:
                    score += 2
                    highlights.append("Excellent food experiences")
        
        dest_info["score"] = score
        dest_info["highlights"] = highlights
        comparison["comparison_results"][destination.lower()] = dest_info
    
    # Determine recommendation
    if comparison["comparison_results"]:
        best_destination = max(comparison["comparison_results"].values(), key=lambda x: x["score"])
        comparison["recommendation"] = {
            "best_match": best_destination["city"],
            "score": best_destination["score"],
            "reasons": best_destination["highlights"]
        }
    
    return comparison

# Create the super travel planner agent
travel_planner_agent = Agent(
    name="travel_planner_super_agent",
    model=MODEL_NAME,
    description=(
        "Comprehensive travel planning agent that coordinates flights, hotels, and activities to create "
        "complete travel itineraries. Specializes in Indian destinations and provides budget-aware recommendations."
    ),
    instruction=(
        "You are an expert travel planner who helps users create comprehensive travel plans. "
        "You coordinate between flight booking, hotel reservations, and activity planning to provide "
        "complete itineraries. You can:\n\n"
        "1. Create full travel plans with flights, accommodation, and activities\n"
        "2. Work within specified budgets and preferences\n"
        "3. Provide cost breakdowns and budget analysis\n"
        "4. Compare multiple destinations to help users decide\n"
        "5. Suggest activities based on interests (adventure, cultural, culinary, etc.)\n"
        "6. Give travel recommendations and tips\n\n"
        "Always consider user preferences, budget constraints, and trip duration when making recommendations. "
        "Provide detailed explanations for your suggestions and offer alternative options when possible. "
        "Be helpful, informative, and ensure all recommendations are practical and well-reasoned."
    ),
    tools=[
        create_comprehensive_travel_plan,
        search_destination_activities,
        get_travel_inspiration,
        compare_destinations,
        # Include individual agent tools for specific queries
        search_flights,
        search_hotels,
        search_activities,
        get_activities_by_category
    ],
)

# Export as root_agent for Google ADK compatibility
root_agent = travel_planner_agent