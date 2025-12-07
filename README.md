# Autonomous Travel Planner

A comprehensive AI-powered travel planning system that coordinates flights, hotels, and activities to create complete travel itineraries for destinations across India.

## Features

### 🌟 Super Travel Planner Agent
The main autonomous agent that coordinates all sub-agents to provide:
- Complete travel itineraries with flights, hotels, and activities
- Budget-aware recommendations and cost breakdowns
- Multi-destination comparisons
- Preference-based planning (luxury, budget, adventure, cultural)
- Activity-based travel inspiration

### 🛫 Flight Agent
- Search flights between Indian cities
- Price and schedule information
- Multiple airline options

### 🏨 Hotel Agent
- Hotel search with rating and price filters
- Accommodation across tourist destinations
- Amenity and location details

### 🎯 Activities Agent
- Activity search by city and category
- Adventure, heritage, culinary experiences
- Duration, pricing, and rating information

## Quick Start

### 1. Install Dependencies
```bash
pip install google-adk>=1.20.0 litellm>=1.80.5
```

### 2. Run the Web Interface
```bash
# Activate your virtual environment
source .venv/bin/activate

# Start the travel planner web interface
adk web travel_planner
```

Access the agent at: http://127.0.0.1:8000

### 3. Run Individual Agents
```bash
# Flight booking agent
adk web flight_agent

# Hotel booking agent  
adk web hotel_agent

# Activities booking agent
adk web activities_agent
```

### 4. Python Script Usage
```bash
python main.py
```

## Usage Examples

### Comprehensive Travel Planning
```
"Plan a 5-day family trip from Delhi to Goa for 4 people. Travel dates: Jan 15-20, 2026. Budget is ₹80,000. We prefer mid-range hotels and adventure activities."
```

### Destination Comparison
```
"Compare Goa, Manali, and Kerala for a 4-day adventure trip. Budget is ₹40,000 per person."
```

### Budget Planning
```
"I'm a student with ₹15,000 budget for a 3-day trip from Mumbai. Suggest budget-friendly destinations with cultural experiences."
```

### Activity-Based Inspiration
```
"Show me destinations across India for heritage and cultural experiences."
```

## Available Destinations

- **Delhi** - Capital city with heritage sites
- **Mumbai** - Financial capital with coastal attractions
- **Bangalore** - Tech hub with pleasant climate
- **Goa** - Beach destination with adventure sports
- **Jaipur** - Pink city with royal heritage
- **Udaipur** - Lake city with palace stays
- **Manali** - Hill station with adventure activities
- **Kerala** - Backwaters and Ayurveda experiences

## Activity Categories

- **Adventure** - Trekking, paragliding, water sports
- **Heritage** - Historical sites, museums, palaces
- **Culinary** - Food tours, cooking classes
- **Nature** - Wildlife, gardens, scenic spots
- **Spiritual** - Temples, meditation, yoga

## Architecture

```
Travel Planner Agent (Super Agent)
├── Flight Agent
│   ├── Flight Search
│   └── Mock Flight Database
├── Hotel Agent  
│   ├── Hotel Search
│   └── Mock Hotel Database
└── Activities Agent
    ├── Activity Search
    ├── Category Filtering
    └── Mock Activities Database
```

## Key Functions

### Super Agent Functions
- `create_comprehensive_travel_plan()` - Complete trip planning
- `compare_destinations()` - Multi-destination comparison
- `search_destination_activities()` - Activity search by destination
- `get_travel_inspiration()` - Category-based inspiration

### Individual Agent Functions
- `search_flights()` - Flight search between cities
- `search_hotels()` - Hotel search with filters
- `search_activities()` - Activity search with filters
- `get_activities_by_category()` - Category-based activity search

## Sample Interaction

**User:** "Plan a romantic honeymoon trip to Udaipur for 4 days from Bangalore. We prefer luxury accommodation and cultural experiences."

**Travel Planner:** Creates a comprehensive plan including:
- Round-trip flights from Bangalore to Udaipur
- Luxury palace hotels like Taj Lake Palace
- Cultural activities like city palace tours
- Cost breakdown and recommendations
- Travel tips and booking advice

## Contributing

This project uses Google ADK (Agent Development Kit) for building AI agents. Each agent specializes in a specific domain while the super agent coordinates them for comprehensive travel planning.

## Environment Setup

1. Create a `.env` file with your API keys if needed
2. Ensure Python 3.11+ is installed
3. Install dependencies via pip or uv
4. Run agents individually or use the super agent for complete planning