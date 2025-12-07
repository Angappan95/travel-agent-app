import datetime
from typing import Optional

from google.adk.agents import Agent
from .mock_data import FLIGHTS_DB, get_all_cities
from config import MODEL_NAME

def search_flights(source: str, destination: str, date: Optional[str] = None) -> dict:
    """Searches for available flights between two cities.

    Args:
        source (str): The departure city.
        destination (str): The arrival city.
        date (str, optional): The travel date in YYYY-MM-DD format. Defaults to today.

    Returns:
        dict: status and list of available flights or error message.
    """

    key = (source.lower(), destination.lower())
    
    if key not in FLIGHTS_DB:

        return {
            "status": "error",
            "error_message": f"No flights available from {source} to {destination}."
        }
    
    flights = FLIGHTS_DB[key]
    travel_date = date if date else datetime.datetime.now().strftime("%Y-%m-%d")
    
    return {
        "status": "success",
        "flights": flights,
        "route": f"{source} to {destination}",
        "date": travel_date
    }

flight_agent = Agent(
    name="flight_booking_agent",
    model=MODEL_NAME,
    description=(
        "Flight booking agent that can search for flights between cities across India."
    ),
    instruction=(
        "You are a helpful flight booking agent who specializes in finding flights between cities. "
        "When users ask about flights, provide them with available options including flight numbers, "
        "departure/arrival times, prices, and airlines. Help users find the best flight options "
        "based on their travel preferences, budget, and schedule. Always be helpful and provide "
        "clear information about available flight options."
    ),
    tools=[search_flights],
)

# Export as root_agent for Google ADK compatibility
root_agent = flight_agent