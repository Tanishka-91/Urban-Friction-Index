# modules/recommendation_engine.py

def get_recommendation(zone_data):

    recs = []

    if zone_data["TrafficScore"] > 60:
        recs.append("🚗 Optimize traffic signals")

    if zone_data["AQIScore"] > 60:
        recs.append("💨 Pollution control measures")

    if zone_data["RoadScore"] > 60:
        recs.append("🛣️ Repair roads and potholes")

    if zone_data["TransportScore"] > 60:
        recs.append("🚌 Increase public transport frequency")

    if not recs:
        recs.append("✅ Area performing well")

    return recs