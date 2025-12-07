import datetime
from typing import Optional, List
import logging

from google.adk.agents import Agent
from flight_agent.agent import search_flights
from hotel_agent.agent import search_hotels
from activities_agent.agent import search_activities, get_activities_by_category
from config import MODEL_NAME

# Setup logger for travel planner
logger = logging.getLogger('travel_agent.travel_planner')

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
    logger.info(f"Starting comprehensive travel plan creation: {source} -> {destination}, {travelers} travelers, budget: {budget}")
    
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
    try:
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
        logger.info(f"Searching for outbound flights: {source} -> {destination} on {travel_date}")
        outbound_flights = search_flights(source, destination, travel_date)
        logger.info(f"Outbound flights search status: {outbound_flights.get('status', 'unknown')}")
        
        # Log outbound flight selection details
        if outbound_flights.get('status') == 'success' and outbound_flights.get('flights'):
            logger.info(f"✈️ OUTBOUND FLIGHTS FOUND: {len(outbound_flights['flights'])} options available")
            for i, flight in enumerate(outbound_flights['flights'][:3], 1):  # Log top 3 options
                logger.info(f"   Option {i}: {flight['airline']} {flight['flight_number']} - {flight['departure']} to {flight['arrival']} - {flight['price']} ({flight['duration']})")
        else:
            logger.warning(f"❌ No outbound flights found for {source} -> {destination} on {travel_date}")
        
        logger.info(f"Searching for return flights: {destination} -> {source} on {return_date}")
        return_flights = search_flights(destination, source, return_date)
        logger.info(f"Return flights search status: {return_flights.get('status', 'unknown')}")
        
        # Log return flight selection details
        if return_flights.get('status') == 'success' and return_flights.get('flights'):
            logger.info(f"✈️ RETURN FLIGHTS FOUND: {len(return_flights['flights'])} options available")
            for i, flight in enumerate(return_flights['flights'][:3], 1):  # Log top 3 options
                logger.info(f"   Option {i}: {flight['airline']} {flight['flight_number']} - {flight['departure']} to {flight['arrival']} - {flight['price']} ({flight['duration']})")
        else:
            logger.warning(f"❌ No return flights found for {destination} -> {source} on {return_date}")

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
        
        logger.info(f"Searching for hotels in {destination} with filters: {hotel_filters}")
        hotels = search_hotels(
            destination, 
            travel_date, 
            return_date,
            **hotel_filters
        )
        logger.info(f"Hotels search status: {hotels.get('status', 'unknown')}")
        
        # Log hotel selection details
        if hotels.get('status') == 'success' and hotels.get('hotels'):
            logger.info(f"🏨 HOTELS FOUND: {len(hotels['hotels'])} options available in {destination}")
            for i, hotel in enumerate(hotels['hotels'][:3], 1):  # Log top 3 options
                logger.info(f"   Option {i}: {hotel['name']} - {hotel['price_per_night']}/night - Rating: {hotel['rating']}/5 - {hotel['amenities'][:2] if hotel['amenities'] else 'No amenities listed'}")
            
            # Log the selected hotel (cheapest one) for cost calculation
            cheapest_hotel = min(hotels['hotels'], key=lambda h: int(h['price_per_night'].replace('₹', '').replace(',', '')))
            logger.info(f"🏆 SELECTED HOTEL FOR COST CALC: {cheapest_hotel['name']} at {cheapest_hotel['price_per_night']}/night (cheapest option)")
        else:
            logger.warning(f"❌ No hotels found in {destination} matching criteria: {hotel_filters}")

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
        
        logger.info(f"Searching for activities in {destination} with filters: {activity_filters}")
        activities = search_activities(destination, **activity_filters)
        logger.info(f"Activities search status: {activities.get('status', 'unknown')}")
        
        # Log activity selection details
        if activities.get('status') == 'success' and activities.get('activities'):
            logger.info(f"🎯 ACTIVITIES FOUND: {len(activities['activities'])} options available in {destination}")
            
            # Group activities by category for better logging
            categories = {}
            for activity in activities['activities']:
                cat = activity['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(activity)
            
            for category, acts in categories.items():
                logger.info(f"   {category}: {len(acts)} activities")
                for i, activity in enumerate(acts[:2], 1):  # Log top 2 per category
                    logger.info(f"     • {activity['name']} - {activity['price']} - Rating: {activity['rating']}/5")
            
            # Log free vs paid activities breakdown
            free_activities = [a for a in activities['activities'] if a['price'] == '₹free']
            paid_activities = [a for a in activities['activities'] if a['price'] != '₹free']
            logger.info(f"💰 ACTIVITY PRICING: {len(free_activities)} free, {len(paid_activities)} paid activities")
            
            if paid_activities:
                avg_paid_price = sum([int(a['price'].replace('₹', '').replace(',', '')) for a in paid_activities]) / len(paid_activities)
                logger.info(f"💵 SELECTED ACTIVITIES FOR COST CALC: Average paid activity cost ₹{avg_paid_price:.0f}")
        else:
            logger.warning(f"❌ No activities found in {destination} matching criteria: {activity_filters}")
        
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
            
            # Log flight cost selection
            logger.info(f"💸 FLIGHT COST CALCULATION: Outbound ₹{outbound_cost:,} + Return ₹{return_cost:,} × {travelers} travelers = ₹{flight_cost:,}")
        
        # Hotel costs
        if hotels["status"] == "success" and hotels["hotels"]:
            cheapest_hotel = min(hotels["hotels"], 
                            key=lambda h: int(h["price_per_night"].replace("₹", "").replace(",", "")))
            hotel_cost_per_night = int(cheapest_hotel["price_per_night"].replace("₹", "").replace(",", ""))
            hotel_total_cost = hotel_cost_per_night * duration_days
            cost_breakdown["accommodation"] = f"₹{hotel_total_cost:,} ({duration_days} nights)"
            total_cost_estimate += hotel_total_cost
            
            # Log hotel cost selection
            logger.info(f"💸 HOTEL COST CALCULATION: {cheapest_hotel['name']} at ₹{hotel_cost_per_night:,}/night × {duration_days} nights = ₹{hotel_total_cost:,}")
        
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
            
            # Log activity cost selection
            activities_count = min(total_activities, len(paid_activities))
            logger.info(f"💸 ACTIVITY COST CALCULATION: {activities_count} activities × ₹{avg_activity_cost:,} average = ₹{activity_cost:,} (estimated {activities_per_day} activities/day × {duration_days} days)")
        
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
        
        logger.info(f"Travel plan created successfully. Total cost estimate: {travel_plan['cost_estimate']['total']}")
        return travel_plan
        
    except Exception as e:
        logger.error(f"Error creating comprehensive travel plan: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Failed to create travel plan: {str(e)}"
        }

def search_destination_activities(destination: str, activity_type: Optional[str] = None) -> dict:
    """Search for activities in a specific destination with optional type filtering.
    
    Args:
        destination (str): The destination city.
        activity_type (str, optional): Type of activity (Adventure, Heritage, Culinary, etc.).
        
    Returns:
        dict: Available activities in the destination.
    """
    logger.info(f"Searching destination activities: {destination}, type: {activity_type}")
    
    try:
        result = search_activities(destination)
        
        logger.info(f"Destination activities search completed for {destination}")
        return result
        
    except Exception as e:
        logger.error(f"Error searching destination activities {destination}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error searching activities: {str(e)}"
        }

def get_travel_inspiration(activity_category: str) -> dict:
    """Get travel inspiration based on activity preferences across all destinations.
    
    Args:
        activity_category (str): The type of activities you're interested in.
        
    Returns:
        dict: Cities and activities matching your interests.
    """
    logger.info(f"Getting travel inspiration for category: {activity_category}")
    
    try:
        result = get_activities_by_category(activity_category)
        logger.info(f"Travel inspiration search completed for {activity_category}")
        return result
        
    except Exception as e:
        logger.error(f"Error getting travel inspiration for {activity_category}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error getting inspiration: {str(e)}"
        }

def compare_destinations(destinations: List[str], preferences: Optional[str] = None) -> dict|None:
    """Compare multiple destinations based on available activities and accommodations.
    
    Args:
        destinations (List[str]): List of destination cities to compare.
        preferences (str, optional): Travel preferences to filter comparison.
        
    Returns:
        dict: Comparison of destinations with recommendations.
    """
    logger.info(f"Comparing destinations: {destinations}, preferences: {preferences}")
    
    try:
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
            
            logger.info(f"Destinations comparison completed. Best match: {comparison.get('recommendation', {}).get('best_match', 'None')}")
            return comparison
        
    except Exception as e:
        logger.error(f"Error comparing destinations {destinations}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error comparing destinations: {str(e)}"
        }

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