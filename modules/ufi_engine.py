import pandas as pd

traffic = pd.read_csv("outputs/traffic_scores.csv")
aqi = pd.read_csv("outputs/aqi_scores.csv")
road = pd.read_csv("outputs/road_scores.csv")
transport = pd.read_csv("outputs/transport_scores.csv")

final_df = traffic.merge(aqi, on="Zone")
final_df = final_df.merge(road, on="Zone")
final_df = final_df.merge(transport, on="Zone")

final_df["UFI"] = (
    0.40 * final_df["TrafficScore"]
    + 0.25 * final_df["AQIScore"]
    + 0.20 * final_df["RoadScore"]
    + 0.15 * final_df["TransportScore"]
)

print("\nUrban Friction Index:\n")
print(final_df)

final_df.to_csv(
    "outputs/final_ufi.csv",
    index=False
)

def get_recommendation(row):

    recommendations = []

    if row["TrafficScore"] > 35:
        recommendations.append(
            "Improve traffic management"
        )

    if row["AQIScore"] > 30:
        recommendations.append(
            "Control pollution sources"
        )

    if row["RoadScore"] > 50:
        recommendations.append(
            "Repair roads and potholes"
        )

    if row["TransportScore"] > 50:
        recommendations.append(
            "Increase public transport frequency"
        )

    return ", ".join(recommendations)

final_df["Recommendation"] = final_df.apply(
    get_recommendation,
    axis=1
)

print(final_df)

final_df.to_csv(
    "outputs/final_ufi.csv",
    index=False
)