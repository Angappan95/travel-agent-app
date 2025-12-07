"""Mock flight data for the travel agent application."""

# Mock flight database - Tourist cities across India
FLIGHTS_DB = {
    # Metro cities
    ("delhi", "mumbai"): [
        {"flight_number": "AI131", "departure": "06:00", "arrival": "08:30", "price": "₹8,500", "airline": "Air India"},
        {"flight_number": "6E2131", "departure": "14:30", "arrival": "17:00", "price": "₹7,200", "airline": "IndiGo"},
    ],
    ("delhi", "bangalore"): [
        {"flight_number": "SG8157", "departure": "09:15", "arrival": "12:45", "price": "₹9,800", "airline": "SpiceJet"},
        {"flight_number": "UK955", "departure": "19:00", "arrival": "22:30", "price": "₹11,200", "airline": "Vistara"},
    ],
    ("mumbai", "delhi"): [
        {"flight_number": "AI860", "departure": "07:30", "arrival": "10:00", "price": "₹8,800", "airline": "Air India"},
        {"flight_number": "6E2142", "departure": "21:15", "arrival": "23:45", "price": "₹7,500", "airline": "IndiGo"},
    ],
    ("mumbai", "bangalore"): [
        {"flight_number": "SG134", "departure": "11:20", "arrival": "13:15", "price": "₹6,500", "airline": "SpiceJet"},
        {"flight_number": "UK864", "departure": "16:45", "arrival": "18:40", "price": "₹8,200", "airline": "Vistara"},
    ],
    ("bangalore", "delhi"): [
        {"flight_number": "AI506", "departure": "05:45", "arrival": "08:30", "price": "₹10,200", "airline": "Air India"},
        {"flight_number": "6E5327", "departure": "15:30", "arrival": "18:15", "price": "₹9,100", "airline": "IndiGo"},
    ],
    ("bangalore", "mumbai"): [
        {"flight_number": "AI652", "departure": "12:00", "arrival": "13:55", "price": "₹6,800", "airline": "Air India"},
        {"flight_number": "UK871", "departure": "20:10", "arrival": "22:05", "price": "₹7,900", "airline": "Vistara"},
    ],
    
    # Tourist destinations
    ("delhi", "goa"): [
        {"flight_number": "AI439", "departure": "08:15", "arrival": "10:45", "price": "₹12,500", "airline": "Air India"},
        {"flight_number": "6E6671", "departure": "16:20", "arrival": "18:50", "price": "₹10,800", "airline": "IndiGo"},
    ],
    ("goa", "delhi"): [
        {"flight_number": "AI440", "departure": "11:30", "arrival": "14:00", "price": "₹12,200", "airline": "Air India"},
        {"flight_number": "6E6672", "departure": "19:45", "arrival": "22:15", "price": "₹11,100", "airline": "IndiGo"},
    ],
    ("mumbai", "goa"): [
        {"flight_number": "SG8723", "departure": "07:00", "arrival": "08:15", "price": "₹5,500", "airline": "SpiceJet"},
        {"flight_number": "6E783", "departure": "18:30", "arrival": "19:45", "price": "₹4,800", "airline": "IndiGo"},
    ],
    ("goa", "mumbai"): [
        {"flight_number": "SG8724", "departure": "09:00", "arrival": "10:15", "price": "₹5,200", "airline": "SpiceJet"},
        {"flight_number": "6E784", "departure": "20:30", "arrival": "21:45", "price": "₹4,900", "airline": "IndiGo"},
    ],
    
    ("delhi", "jaipur"): [
        {"flight_number": "AI9614", "departure": "07:30", "arrival": "08:45", "price": "₹6,800", "airline": "Air India"},
        {"flight_number": "6E2423", "departure": "17:15", "arrival": "18:30", "price": "₹5,900", "airline": "IndiGo"},
    ],
    ("jaipur", "delhi"): [
        {"flight_number": "AI9615", "departure": "09:30", "arrival": "10:45", "price": "₹6,500", "airline": "Air India"},
        {"flight_number": "6E2424", "departure": "19:00", "arrival": "20:15", "price": "₹6,200", "airline": "IndiGo"},
    ],
    
    ("delhi", "udaipur"): [
        {"flight_number": "AI473", "departure": "10:20", "arrival": "11:50", "price": "₹9,200", "airline": "Air India"},
        {"flight_number": "6E2141", "departure": "14:45", "arrival": "16:15", "price": "₹8,100", "airline": "IndiGo"},
    ],
    ("udaipur", "delhi"): [
        {"flight_number": "AI474", "departure": "12:30", "arrival": "14:00", "price": "₹8,900", "airline": "Air India"},
        {"flight_number": "6E2142", "departure": "17:00", "arrival": "18:30", "price": "₹8,300", "airline": "IndiGo"},
    ],
    
    ("mumbai", "udaipur"): [
        {"flight_number": "SG8429", "departure": "13:15", "arrival": "14:45", "price": "₹7,800", "airline": "SpiceJet"},
        {"flight_number": "UK883", "departure": "16:30", "arrival": "18:00", "price": "₹9,100", "airline": "Vistara"},
    ],
    ("udaipur", "mumbai"): [
        {"flight_number": "SG8430", "departure": "15:30", "arrival": "17:00", "price": "₹7,600", "airline": "SpiceJet"},
        {"flight_number": "UK884", "departure": "18:45", "arrival": "20:15", "price": "₹8,800", "airline": "Vistara"},
    ],
    
    ("bangalore", "goa"): [
        {"flight_number": "AI2814", "departure": "09:45", "arrival": "10:50", "price": "₹6,200", "airline": "Air India"},
        {"flight_number": "6E5089", "departure": "15:20", "arrival": "16:25", "price": "₹5,400", "airline": "IndiGo"},
    ],
    ("goa", "bangalore"): [
        {"flight_number": "AI2815", "departure": "11:45", "arrival": "12:50", "price": "₹5,900", "airline": "Air India"},
        {"flight_number": "6E5090", "departure": "17:15", "arrival": "18:20", "price": "₹5,700", "airline": "IndiGo"},
    ],
    
    ("delhi", "manali"): [
        {"flight_number": "AI9809", "departure": "06:45", "arrival": "08:15", "price": "₹11,500", "airline": "Air India"},
        {"flight_number": "SG8467", "departure": "14:30", "arrival": "16:00", "price": "₹9,800", "airline": "SpiceJet"},
    ],
    ("manali", "delhi"): [
        {"flight_number": "AI9810", "departure": "09:00", "arrival": "10:30", "price": "₹11,200", "airline": "Air India"},
        {"flight_number": "SG8468", "departure": "17:00", "arrival": "18:30", "price": "₹10,100", "airline": "SpiceJet"},
    ],
    
    ("mumbai", "kerala"): [
        {"flight_number": "AI689", "departure": "08:00", "arrival": "10:15", "price": "₹8,900", "airline": "Air India"},
        {"flight_number": "6E345", "departure": "15:45", "arrival": "18:00", "price": "₹7,600", "airline": "IndiGo"},
    ],
    ("kerala", "mumbai"): [
        {"flight_number": "AI690", "departure": "11:00", "arrival": "13:15", "price": "₹8,700", "airline": "Air India"},
        {"flight_number": "6E346", "departure": "19:30", "arrival": "21:45", "price": "₹7,900", "airline": "IndiGo"},
    ],
    
    ("delhi", "kashmir"): [
        {"flight_number": "AI441", "departure": "07:15", "arrival": "08:45", "price": "₹13,800", "airline": "Air India"},
        {"flight_number": "6E2355", "departure": "13:30", "arrival": "15:00", "price": "₹12,100", "airline": "IndiGo"},
    ],
    ("kashmir", "delhi"): [
        {"flight_number": "AI442", "departure": "09:30", "arrival": "11:00", "price": "₹13,500", "airline": "Air India"},
        {"flight_number": "6E2356", "departure": "16:00", "arrival": "17:30", "price": "₹12,400", "airline": "IndiGo"},
    ],
    
    ("mumbai", "kashmir"): [
        {"flight_number": "UK867", "departure": "10:15", "arrival": "12:30", "price": "₹15,200", "airline": "Vistara"},
        {"flight_number": "SG3421", "departure": "16:45", "arrival": "19:00", "price": "₹13,900", "airline": "SpiceJet"},
    ],
    ("kashmir", "mumbai"): [
        {"flight_number": "UK868", "departure": "13:15", "arrival": "15:30", "price": "₹14,800", "airline": "Vistara"},
        {"flight_number": "SG3422", "departure": "19:45", "arrival": "22:00", "price": "₹14,200", "airline": "SpiceJet"},
    ],
}

def get_all_cities():
    """Returns a list of all cities in the flight database."""
    cities = set()
    for route in FLIGHTS_DB.keys():
        cities.add(route[0])
        cities.add(route[1])
    return sorted(list(cities))
