import datetime
from typing import Optional
import logging

from google.adk.agents import Agent
from .mock_data import HOTELS_DB, get_hotel_cities
from config import MODEL_NAME

# Setup logger for hotel agent
logger = logging.getLogger('travel_agent.hotel_agent')

def search_hotels(city: str, checkin_date: Optional[str] = None, checkout_date: Optional[str] = None, 
                 max_price: Optional[int] = None, min_rating: Optional[int] = None) -> dict:
    """Searches for available hotels in a city with optional filters.

    Args:
        city (str): The city to search for hotels.
        checkin_date (str, optional): Check-in date in YYYY-MM-DD format. Defaults to today.
        checkout_date (str, optional): Check-out date in YYYY-MM-DD format. Defaults to tomorrow.
        max_price (int, optional): Maximum price per night in rupees. 
        min_rating (int, optional): Minimum hotel rating (1-5 stars).

    Returns:
        dict: status and list of available hotels or error message.
    """
    logger.info(f"Searching hotels in {city}, filters: max_price={max_price}, min_rating={min_rating}")
    
    try:
        city_key = city.lower()
        
        # Check if city exists in hotels database
        if city_key not in HOTELS_DB:
            available_cities = get_hotel_cities()
            logger.warning(f"No hotels available in {city}. Available cities: {available_cities}")
            return {
                "status": "error",
                "error_message": f"No hotels available in {city.title()}. Available cities: {', '.join([c.title() for c in available_cities])}"
            }
        
        # Set default dates
        if not checkin_date:
            checkin_date = datetime.datetime.now().strftime("%Y-%m-%d")
        if not checkout_date:
            checkout_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        
        # Get all hotels for the city
        all_hotels = HOTELS_DB[city_key]
        filtered_hotels = []
        logger.info(f"Found {len(all_hotels)} total hotels in {city}, applying filters...")
        
        # Apply filters
        for hotel in all_hotels:
            # Price filter
            if max_price:
                hotel_price = int(hotel["price_per_night"].replace("₹", "").replace(",", ""))
                if hotel_price > max_price:
                    continue
            
            # Rating filter
            if min_rating and hotel["rating"] < min_rating:
                continue
                
            filtered_hotels.append(hotel)
    
        if not filtered_hotels:
            logger.warning(f"No hotels found in {city} matching criteria")
            return {
                "status": "error", 
                "error_message": f"No hotels found in {city.title()} matching your criteria. Try adjusting your filters."
            }
        
        # Sort by rating (highest first), then by price (lowest first)
        filtered_hotels.sort(key=lambda h: (-h["rating"], int(h["price_per_night"].replace("₹", "").replace(",", ""))))
        
        logger.info(f"Hotel search completed for {city}: {len(filtered_hotels)} hotels found")
        
        return {
            "status": "success",
            "city": city.title(),
            "checkin_date": checkin_date,
            "checkout_date": checkout_date,
            "hotels_found": len(filtered_hotels),
            "hotels": filtered_hotels,
            "filters_applied": {
                "max_price": f"₹{max_price:,}" if max_price else "None",
                "min_rating": f"{min_rating} stars" if min_rating else "None"
            }
        }
        
    except Exception as e:
        logger.error(f"Error searching hotels in {city}: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error_message": f"Error searching hotels: {str(e)}"
        }

hotel_agent = Agent(
    name="hotel_booking_agent",
    model=MODEL_NAME,
    description=(
        "Hotel booking agent that can search for accommodations across tourist cities in India."
    ),
    instruction=(
        "You are a helpful hotel booking agent who specializes in finding accommodations. "
        "When users ask about hotels, show them available accommodations with ratings, prices, "
        "amenities, and locations. You can apply filters like price range and minimum rating. "
        "Provide detailed information about hotel amenities, locations, and help users choose "
        "the best option based on their preferences and budget. Always be helpful and informative."
    ),
    tools=[search_hotels],
)

# Export as root_agent for Google ADK compatibility
root_agent = hotel_agent
