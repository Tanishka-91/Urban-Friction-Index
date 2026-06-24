def get_recommendation(row):

    scores = {
        "Traffic": row["TrafficScore"],
        "AQI": row["AQIScore"],
        "Road": row["RoadScore"],
        "Transport": row["TransportScore"]
    }

    highest = max(
        scores,
        key=scores.get
    )

    if highest == "Traffic":
        return "Increase signal timing and traffic management."

    elif highest == "AQI":
        return "Implement pollution control measures."

    elif highest == "Road":
        return "Repair roads and fix potholes."

    elif highest == "Transport":
        return "Increase bus frequency and route coverage."

    return "Monitor conditions."