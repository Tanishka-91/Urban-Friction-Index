import pandas as pd

traffic = pd.read_csv("outputs/traffic_scores.csv")
aqi = pd.read_csv("outputs/aqi_scores.csv")
road = pd.read_csv("outputs/road_scores2.csv")
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

# print("\nUrban Friction Index:\n")
# print(final_df)

final_df.to_csv(
    "outputs/final_ufi.csv",
    index=False
)

print(final_df)