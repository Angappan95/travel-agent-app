"""Mock activities data for the travel agent application."""

# Mock activities database - Fun activities in tourist cities across India
ACTIVITIES_DB = {
    "delhi": [
        {"name": "Red Fort Historical Tour", "category": "Heritage", "duration": "3 hours", "price": "₹800", "rating": 4.5, "description": "Explore the magnificent Mughal architecture and history"},
        {"name": "India Gate Cycling Tour", "category": "Adventure", "duration": "2 hours", "price": "₹600", "rating": 4.2, "description": "Cycle around India Gate and Rajpath with guided commentary"},
        {"name": "Old Delhi Food Walk", "category": "Culinary", "duration": "4 hours", "price": "₹1,200", "rating": 4.8, "description": "Taste authentic street food in Chandni Chowk"},
        {"name": "Kingdom of Dreams Show", "category": "Entertainment", "duration": "2.5 hours", "price": "₹2,500", "rating": 4.3, "description": "Bollywood musical and cultural performances"},
    ],
    "mumbai": [
        {"name": "Marine Drive Evening Walk", "category": "Leisure", "duration": "2 hours", "price": "₹free", "rating": 4.6, "description": "Stroll along the Queen's Necklace with sunset views"},
        {"name": "Elephanta Caves Ferry Trip", "category": "Heritage", "duration": "6 hours", "price": "₹1,500", "rating": 4.4, "description": "Ferry ride and ancient cave temples exploration"},
        {"name": "Bollywood Studio Tour", "category": "Entertainment", "duration": "4 hours", "price": "₹3,200", "rating": 4.7, "description": "Behind-the-scenes look at Bollywood film making"},
        {"name": "Dharavi Slum Tour", "category": "Cultural", "duration": "3 hours", "price": "₹1,800", "rating": 4.5, "description": "Educational tour of Asia's largest slum community"},
    ],
    "bangalore": [
        {"name": "Nandi Hills Sunrise Trek", "category": "Adventure", "duration": "4 hours", "price": "₹1,000", "rating": 4.6, "description": "Early morning trek to catch spectacular sunrise views"},
        {"name": "Bangalore Palace Tour", "category": "Heritage", "duration": "2 hours", "price": "₹500", "rating": 4.3, "description": "Explore the Tudor-style architecture and royal artifacts"},
        {"name": "Microbrewery Pub Crawl", "category": "Nightlife", "duration": "4 hours", "price": "₹2,800", "rating": 4.5, "description": "Visit 3-4 craft beer breweries with guided tasting"},
        {"name": "Cubbon Park Nature Walk", "category": "Nature", "duration": "2 hours", "price": "₹300", "rating": 4.1, "description": "Guided walk through the city's green lung"},
    ],
    "goa": [
        {"name": "Parasailing at Calangute Beach", "category": "Water Sports", "duration": "1 hour", "price": "₹2,500", "rating": 4.7, "description": "Soar high above the Arabian Sea with stunning coastal views"},
        {"name": "Sunset Dolphin Cruise", "category": "Wildlife", "duration": "3 hours", "price": "₹1,800", "rating": 4.8, "description": "Spot dolphins while enjoying sunset over the ocean"},
        {"name": "Spice Plantation Tour", "category": "Nature", "duration": "5 hours", "price": "₹1,200", "rating": 4.4, "description": "Learn about spice cultivation with traditional Goan lunch"},
        {"name": "Casino Royale Night", "category": "Entertainment", "duration": "4 hours", "price": "₹4,000", "rating": 4.2, "description": "Try your luck at offshore floating casinos"},
    ],
    "jaipur": [
        {"name": "Hot Air Balloon Ride", "category": "Adventure", "duration": "3 hours", "price": "₹12,000", "rating": 4.9, "description": "Aerial views of Amber Fort and Pink City landscape"},
        {"name": "Amber Fort Elephant Ride", "category": "Heritage", "duration": "2 hours", "price": "₹1,500", "rating": 4.0, "description": "Traditional elephant ride up to the majestic fort"},
        {"name": "Rajasthani Cooking Class", "category": "Culinary", "duration": "4 hours", "price": "₹2,200", "rating": 4.6, "description": "Learn to cook authentic Rajasthani dishes"},
        {"name": "Chokhi Dhani Village Experience", "category": "Cultural", "duration": "5 hours", "price": "₹3,500", "rating": 4.4, "description": "Traditional Rajasthani village life with folk shows"},
    ],
    "udaipur": [
        {"name": "Lake Pichola Boat Ride", "category": "Leisure", "duration": "2 hours", "price": "₹1,000", "rating": 4.7, "description": "Romantic boat ride with palace views"},
        {"name": "City Palace Heritage Walk", "category": "Heritage", "duration": "3 hours", "price": "₹1,800", "rating": 4.5, "description": "Explore the largest palace complex in Rajasthan"},
        {"name": "Vintage Car Museum Tour", "category": "Culture", "duration": "1.5 hours", "price": "₹800", "rating": 4.2, "description": "See the royal collection of classic automobiles"},
        {"name": "Monsoon Palace Sunset Trek", "category": "Adventure", "duration": "3 hours", "price": "₹1,500", "rating": 4.6, "description": "Hike to hilltop palace for panoramic sunset views"},
    ],
    "manali": [
        {"name": "Solang Valley Paragliding", "category": "Adventure", "duration": "2 hours", "price": "₹3,500", "rating": 4.8, "description": "Tandem paragliding with Himalayan mountain views"},
        {"name": "Rohtang Pass Snow Activities", "category": "Adventure", "duration": "6 hours", "price": "₹2,800", "rating": 4.6, "description": "Skiing, snowboarding, and snow scooter rides"},
        {"name": "Beas River Rafting", "category": "Water Sports", "duration": "4 hours", "price": "₹2,200", "rating": 4.5, "description": "White water rafting through scenic valleys"},
        {"name": "Hadimba Temple Forest Walk", "category": "Spiritual", "duration": "2 hours", "price": "₹500", "rating": 4.3, "description": "Peaceful walk through cedar forests to ancient temple"},
    ],
    "kerala": [
        {"name": "Backwater Houseboat Cruise", "category": "Leisure", "duration": "8 hours", "price": "₹8,000", "rating": 4.9, "description": "Traditional kettuvallam cruise through palm-fringed canals"},
        {"name": "Periyar Wildlife Safari", "category": "Wildlife", "duration": "4 hours", "price": "₹2,500", "rating": 4.6, "description": "Spot elephants, tigers and exotic birds in Thekkady"},
        {"name": "Ayurvedic Spa Treatment", "category": "Wellness", "duration": "3 hours", "price": "₹4,500", "rating": 4.7, "description": "Traditional Kerala massage and herbal treatments"},
        {"name": "Tea Plantation Tour in Munnar", "category": "Nature", "duration": "5 hours", "price": "₹1,800", "rating": 4.4, "description": "Learn about tea processing with tasting sessions"},
    ],
    "kashmir": [
        {"name": "Gulmarg Gondola Cable Car", "category": "Adventure", "duration": "4 hours", "price": "₹2,200", "rating": 4.8, "description": "World's second-highest operating cable car ride"},
        {"name": "Dal Lake Shikara Ride", "category": "Leisure", "duration": "2 hours", "price": "₹1,200", "rating": 4.7, "description": "Traditional boat ride on the famous lake"},
        {"name": "Skiing at Gulmarg", "category": "Adventure", "duration": "6 hours", "price": "₹5,500", "rating": 4.6, "description": "World-class skiing on pristine Himalayan slopes"},
        {"name": "Mughal Gardens Tour", "category": "Heritage", "duration": "3 hours", "price": "₹800", "rating": 4.4, "description": "Visit Shalimar, Nishat and Chashme Shahi gardens"},
    ],
}

def get_activity_cities():
    """Returns a list of all cities with available activities."""
    return sorted(list(ACTIVITIES_DB.keys()))

def get_activity_categories():
    """Returns a list of all activity categories."""
    categories = set()
    for city_activities in ACTIVITIES_DB.values():
        for activity in city_activities:
            categories.add(activity["category"])
    return sorted(list(categories))