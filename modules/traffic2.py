import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/traffic.csv")

# FROM PAPER 1 — weighted vehicle count
df["WeightedVolume"] = (
    df["CarCount"]   * 1.0 +
    df["BikeCount"]  * 0.5 +
    df["BusCount"]   * 2.0 +
    df["TruckCount"] * 3.0
)

# FROM PAPER 2 — heavy vehicle ratio as congestion signal
df["HeavyRatio"] = (
    (df["BusCount"] + df["TruckCount"]) / df["Total"]
)

# FROM PAPER 3 — time period classification
def get_time_period(hour):
    if 7 <= hour <= 10:
        return 1.3   # peak multiplier
    elif 17 <= hour <= 20:
        return 1.3
    else:
        return 1.0   # normal

df["PeakMultiplier"] = df["Hour"].apply(get_time_period)

# COMBINE EVERYTHING
df["FinalScore"] = (
    df["WeightedVolume"] * 
    (1 + df["HeavyRatio"]) * 
    df["PeakMultiplier"]
)

# NORMALIZE TO 0-100
scaler = MinMaxScaler()
df["TrafficScore"] = scaler.fit_transform(
    df[["FinalScore"]]
) * 100

# ZONE-WISE AVERAGE
zone_scores = df.groupby("Zone")["TrafficScore"].mean().reset_index()
print(zone_scores)