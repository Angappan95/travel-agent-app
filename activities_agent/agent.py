from typing import Optional
import logging

from google.adk.agents import Agent
from .mock_data import ACTIVITIES_DB, get_activity_cities, get_activity_categories
from config import MODEL_NAME

# Setup logger for activities agent
logger = logging.getLogger('travel_agent.activities_agent')

def search_activities(city: str, 
                     min_rating: Optional[float] = None,
                     max_price: Optional[int] = None) -> dict:
    """Search for activities in a city with optional rating and price filters.

    Args:
        city (str): The city to search for activities.
        min_rating (float, optional): Minimum activity rating (1-5 stars).
        max_price (int, optional): Maximum price in rupees.

    Returns:
        dict: Status and list of available activities or error message.
    """
    logger.info(f"Searching activities in {city}, filters: min_rating={min_rating}, max_price={max_price}")
    
    try:
        city_key = city.lower()
        
        # Check if city exists in activities database
        if city_key not in ACTIVITIES_DB:
            available_cities = get_activity_cities()
            logger.warning(f"No activities available in {city}. Available cities: {available_cities}")
            return {
                "status": "error",
                "error_message": f"No activities available in {city.title()}. Available cities: {', '.join([c.title() for c in available_cities])}"
            }
        
        # Get all activities for the city
        all_activities = ACTIVITIES_DB[city_key]
        filtered_activities = []
        logger.info(f"Found {len(all_activities)} total activities in {city}, applying filters...")
        
        # Apply filters only if specified
        for activity in all_activities:
            # Rating filter
            if min_rating and activity["rating"] < min_rating:
                continue
                
            # Price filter
            if max_price and activity["price"] != "₹free":
                try:
                    activity_price = int(activity["price"].replace("₹", "").replace(",", ""))
                    if activity_price > max_price:
                        continue
                except ValueError:
                    # Skip if price parsing fails
                    continue
        
        filtered_activities.append(activity)
    
        # Sort by rating (highest first)
        filtered_activities.sort(key=lambda x: x["rating"], reverse=True)
        
        logger.info(f"Activities search completed for {city}: {len(filtered_activities)} activities found")
        
        return {
            "status": "success",
            "city": city.title(),
            "activities_found": len(filtered_activities),
            "activities": filtered_activities,
            "filters_applied": {
                "min_rating": f"{min_rating} stars" if min_rating else "None",
                "max_price": f"₹{max_price:,}" if max_price else "None"
            }
        }
        
    except Exception as e:
        logger.error(f"Error searching activities in {city}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error searching activities: {str(e)}"
        }

def get_all_activities() -> dict:
    """Get all activities across all cities for overview.
    
    Returns:
        dict: All activities organized by city.
    """
    all_cities_activities = {}
    
    for city, activities in ACTIVITIES_DB.items():
        # Sort activities by rating
        sorted_activities = sorted(activities, key=lambda x: x["rating"], reverse=True)
        all_cities_activities[city.title()] = sorted_activities
    
    return {
        "status": "success",
        "total_cities": len(all_cities_activities),
        "cities": list(all_cities_activities.keys()),
        "activities_by_city": all_cities_activities
    }

def get_activities_by_category(category: str) -> dict:
    """Get activities by category across all cities.
    
    Args:
        category (str): The activity category to search for.
        
    Returns:
        dict: Activities matching the category from all cities.
    """
    logger.info(f"Searching activities by category: {category}")
    
    try:
        category_activities = {}
        available_categories = get_activity_categories()
        
        # Check if category exists
        if category not in available_categories:
            logger.warning(f"Category '{category}' not found. Available: {available_categories}")
            return {
                "status": "error",
                "error_message": f"Category '{category}' not found. Available categories: {', '.join(available_categories)}"
            }
        
        # Search for activities in the specified category across all cities
        for city, activities in ACTIVITIES_DB.items():
            matching_activities = [
                activity for activity in activities 
                if activity["category"].lower() == category.lower()
            ]
            
            if matching_activities:
                # Sort by rating (highest first)
                matching_activities.sort(key=lambda x: x["rating"], reverse=True)
                category_activities[city.title()] = matching_activities
        
        logger.info(f"Category search completed: {len(category_activities)} cities have {category} activities")
        
        return {
            "status": "success",
            "category": category,
            "cities_with_activities": len(category_activities),
            "cities": list(category_activities.keys()),
            "activities_by_city": category_activities
        }
        
    except Exception as e:
        logger.error(f"Error searching activities by category {category}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error searching by category: {str(e)}"
        }

activities_agent = Agent(
    name="activities_booking_agent",
    model=MODEL_NAME,
    description=(
        "Activities booking agent that can search for activities and experiences in tourist cities across India."
    ),
    instruction=(
        "You are a helpful activities booking agent. When users ask about activities in a city, "
        "always show them the complete list of activities first using search_activities(city) with no filters. "
        "Each city has 4-5 carefully curated activities with ratings (1-5 stars) and prices. "
        "Only apply rating or price filters if the user specifically asks for them (e.g., 'show me activities with 4+ stars' or 'under ₹2000'). "
        "Always display the activity name, category, duration, price, rating, and description clearly. "
        "Keep your responses simple and focused on the activities available."
    ),
    tools=[search_activities, get_all_activities, get_activities_by_category],
)

# Export as root_agent for Google ADK compatibility
root_agent = activities_agent
