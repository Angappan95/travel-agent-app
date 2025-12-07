"""Mock hotel data for the travel agent application."""

# Mock hotel database - Tourist cities across India
HOTELS_DB = {
    "delhi": [
        {"name": "The Imperial New Delhi", "rating": 5, "price_per_night": "₹15,000", "amenities": ["WiFi", "Pool", "Spa", "Restaurant"], "location": "Connaught Place"},
        {"name": "The Oberoi New Delhi", "rating": 5, "price_per_night": "₹18,000", "amenities": ["WiFi", "Pool", "Gym", "Restaurant", "Bar"], "location": "Golf Links"},
        {"name": "Hotel Tara Palace", "rating": 3, "price_per_night": "₹4,500", "amenities": ["WiFi", "Restaurant", "Room Service"], "location": "Chandni Chowk"},
        {"name": "Bloom Hotel", "rating": 4, "price_per_night": "₹8,200", "amenities": ["WiFi", "Gym", "Restaurant", "Business Center"], "location": "Nehru Place"},
    ],
    "mumbai": [
        {"name": "The Taj Mahal Palace", "rating": 5, "price_per_night": "₹20,000", "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Heritage"], "location": "Gateway of India"},
        {"name": "The Oberoi Mumbai", "rating": 5, "price_per_night": "₹22,000", "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Ocean View"], "location": "Nariman Point"},
        {"name": "Hotel Marine Plaza", "rating": 4, "price_per_night": "₹9,500", "amenities": ["WiFi", "Restaurant", "Bar", "Business Center"], "location": "Marine Drive"},
        {"name": "FabHotel Prime", "rating": 3, "price_per_night": "₹3,800", "amenities": ["WiFi", "AC", "Room Service"], "location": "Andheri"},
    ],
    "bangalore": [
        {"name": "The Leela Palace Bengaluru", "rating": 5, "price_per_night": "₹16,500", "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Garden"], "location": "Airport Road"},
        {"name": "ITC Gardenia", "rating": 5, "price_per_night": "₹14,000", "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Business Center"], "location": "Residency Road"},
        {"name": "Vivanta Bengaluru", "rating": 4, "price_per_night": "₹8,800", "amenities": ["WiFi", "Pool", "Gym", "Restaurant"], "location": "Whitefield"},
        {"name": "Zostel Bangalore", "rating": 3, "price_per_night": "₹1,200", "amenities": ["WiFi", "Common Area", "Kitchen"], "location": "Koramangala"},
    ],
    "goa": [
        {"name": "The Leela Goa", "rating": 5, "price_per_night": "₹25,000", "amenities": ["WiFi", "Beach Access", "Pool", "Spa", "Restaurant"], "location": "Cavelossim Beach"},
        {"name": "Grand Hyatt Goa", "rating": 5, "price_per_night": "₹18,500", "amenities": ["WiFi", "Beach Access", "Pool", "Spa", "Golf"], "location": "Bambolim"},
        {"name": "Pousada by the Beach", "rating": 4, "price_per_night": "₹7,200", "amenities": ["WiFi", "Beach Access", "Restaurant", "Bar"], "location": "Calangute"},
        {"name": "Backpacker Panda", "rating": 2, "price_per_night": "₹800", "amenities": ["WiFi", "Common Kitchen", "Lounge"], "location": "Anjuna"},
    ],
    "jaipur": [
        {"name": "Rambagh Palace", "rating": 5, "price_per_night": "₹35,000", "amenities": ["WiFi", "Heritage", "Pool", "Spa", "Restaurant", "Palace"], "location": "Bhawani Singh Road"},
        {"name": "The Oberoi Rajvilas", "rating": 5, "price_per_night": "₹40,000", "amenities": ["WiFi", "Heritage", "Pool", "Spa", "Villas"], "location": "Goner Road"},
        {"name": "Hotel Pearl Palace", "rating": 3, "price_per_night": "₹3,200", "amenities": ["WiFi", "Restaurant", "Rooftop"], "location": "Hathroi Fort"},
        {"name": "Zostel Jaipur", "rating": 3, "price_per_night": "₹1,500", "amenities": ["WiFi", "Common Area", "Cafe"], "location": "MI Road"},
    ],
    "udaipur": [
        {"name": "The Oberoi Udaivilas", "rating": 5, "price_per_night": "₹45,000", "amenities": ["WiFi", "Lake View", "Heritage", "Pool", "Spa", "Boat"], "location": "Lake Pichola"},
        {"name": "Taj Lake Palace", "rating": 5, "price_per_night": "₹50,000", "amenities": ["WiFi", "Lake Palace", "Heritage", "Spa", "Boat Access"], "location": "Lake Pichola"},
        {"name": "Hotel Lakend", "rating": 4, "price_per_night": "₹6,500", "amenities": ["WiFi", "Lake View", "Restaurant", "Terrace"], "location": "Fateh Sagar Lake"},
        {"name": "Moustache Udaipur", "rating": 3, "price_per_night": "₹2,000", "amenities": ["WiFi", "Cafe", "Common Area"], "location": "Old City"},
    ],
    "manali": [
        {"name": "The Himalayan", "rating": 4, "price_per_night": "₹12,000", "amenities": ["WiFi", "Mountain View", "Spa", "Restaurant", "Fireplace"], "location": "Hadimba Road"},
        {"name": "Snow Valley Resorts", "rating": 4, "price_per_night": "₹8,500", "amenities": ["WiFi", "Mountain View", "Restaurant", "Adventure Sports"], "location": "Solang Valley"},
        {"name": "Hotel Holiday", "rating": 3, "price_per_night": "₹4,200", "amenities": ["WiFi", "Restaurant", "Room Service"], "location": "Mall Road"},
        {"name": "Zostel Manali", "rating": 3, "price_per_night": "₹1,800", "amenities": ["WiFi", "Common Area", "Mountain View"], "location": "Old Manali"},
    ],
    "kerala": [
        {"name": "Kumarakom Lake Resort", "rating": 5, "price_per_night": "₹28,000", "amenities": ["WiFi", "Backwaters", "Ayurveda", "Pool", "Boat"], "location": "Kumarakom"},
        {"name": "Coconut Lagoon", "rating": 5, "price_per_night": "₹22,000", "amenities": ["WiFi", "Heritage", "Backwaters", "Ayurveda", "Traditional"], "location": "Kumarakom"},
        {"name": "Spice Village", "rating": 4, "price_per_night": "₹9,500", "amenities": ["WiFi", "Spice Garden", "Restaurant", "Nature"], "location": "Thekkady"},
        {"name": "Green Palace", "rating": 3, "price_per_night": "₹3,500", "amenities": ["WiFi", "Garden", "Restaurant"], "location": "Munnar"},
    ],
    "kashmir": [
        {"name": "The Khyber Himalayan Resort", "rating": 5, "price_per_night": "₹32,000", "amenities": ["WiFi", "Mountain View", "Spa", "Skiing", "Restaurant"], "location": "Gulmarg"},
        {"name": "Vivanta Dal View", "rating": 5, "price_per_night": "₹24,000", "amenities": ["WiFi", "Lake View", "Spa", "Restaurant", "Shikara"], "location": "Dal Lake"},
        {"name": "Hotel Heevan", "rating": 4, "price_per_night": "₹7,800", "amenities": ["WiFi", "Mountain View", "Restaurant", "Garden"], "location": "Pahalgam"},
        {"name": "Youth Hostel", "rating": 2, "price_per_night": "₹1,500", "amenities": ["Basic WiFi", "Shared Rooms", "Cafeteria"], "location": "Srinagar"},
    ],
}

def get_hotel_cities():
    """Returns a list of all cities with available hotels."""
    return sorted(list(HOTELS_DB.keys()))