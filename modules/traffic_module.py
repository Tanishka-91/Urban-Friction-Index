import pandas as pd

from sklearn.preprocessing import MinMaxScaler

def process_traffic(file_path):
    df = pd.read_csv(file_path)
    df = pd.read_csv("data/traffic.csv")

    df = df.drop_duplicates()

    scaler = MinMaxScaler()

    df["TrafficScore"] = scaler.fit_transform(
        df[["Total"]]
    ) * 100

    df = create_zones(df)

    zone_df = generate_zone_scores(df)

    zone_df.to_csv(
    "outputs/traffic_scores.csv",
    index=False
    )

    return zone_df

def create_zones(df):

    zone_size = len(df) // 5

    zones = []

    for i in range(len(df)):

        if i < zone_size:
            zones.append("Zone A")

        elif i < zone_size * 2:
            zones.append("Zone B")

        elif i < zone_size * 3:
            zones.append("Zone C")

        elif i < zone_size * 4:
            zones.append("Zone D")

        else:
            zones.append("Zone E")

    df["Zone"] = zones

    return df

def generate_zone_scores(df):

    zone_df = (
        df.groupby("Zone")["TrafficScore"]
        .mean()
        .reset_index()
    )

    return zone_df

