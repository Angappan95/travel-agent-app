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

### Prerequisite:
```bash
# Install uv first. Run this command in your terminal:
pip install uv
```

### 1. Install Dependencies
```bash
# Create virtual environment
uv venv

# Install dependencies from pyproject.toml
uv pip install -r pyproject.toml
```

### 2. Run the Web Interface
```bash
# Activate your virtual environment
source .venv/bin/activate

# Start the travel planner web interface
adk web
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
"Plan a 3-day family trip from Delhi to Goa for 2 people. Travel dates: Jan 15-20, 2026. Budget is ₹40,000. We prefer mid-range hotels and adventure activities."
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

## Logging and Flow Tracking

The application includes comprehensive logging to track the flow of operations across all agents:

### Log Configuration
- **Log File**: `travel_agent.log` (created automatically)
- **Log Level**: INFO (configurable via `config.py`)
- **Log Format**: Timestamp, logger name, level, file:line, and message

### Logging Features

#### 1. **Flow Tracking**
- Function entry/exit with execution times
- Agent interactions and handoffs
- Search operations with metrics
- Business events for analytics

#### 2. **Error Handling**
- Comprehensive exception logging with stack traces
- Graceful error recovery
- Error context preservation

#### 3. **Performance Monitoring**
- Function execution times
- Search result counts
- Resource usage patterns

#### 4. **Business Analytics**
- Travel plan requests and completions
- Search patterns and preferences
- Cost analysis tracking

### Log Examples

```
2024-12-07 10:30:15 - travel_agent.travel_planner - INFO - [agent.py:45] - Starting comprehensive travel plan creation: Bangalore -> Udaipur, 2 travelers, budget: 50000
2024-12-07 10:30:15 - travel_agent.flight_agent - INFO - [agent.py:25] - Searching flights: Bangalore -> Udaipur on 2024-12-10
2024-12-07 10:30:16 - travel_agent.hotel_agent - INFO - [agent.py:35] - Searching hotels in Udaipur, filters: max_price=8000, min_rating=4
2024-12-07 10:30:17 - travel_agent.activities_agent - INFO - [agent.py:28] - Searching activities in Udaipur, filters: category=Heritage
2024-12-07 10:30:18 - travel_agent.business_events - INFO - [logging_utils.py:85] - BUSINESS_EVENT: travel_plan_completed | DATA: destination=Udaipur, total_cost=₹48,500, duration=4
```

### Logging Utilities

The `logging_utils.py` module provides:
- **Function decorators** for automatic timing and error logging
- **Context managers** for grouped operations
- **Business event logging** for analytics
- **Search metrics tracking** for performance optimization

## Environment Setup

1. Create a `.env` file with your API keys if needed
2. Ensure Python 3.11+ is installed
3. Install dependencies via pip or uv
4. Run agents individually or use the super agent for complete planning