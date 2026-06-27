import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def process_aqi(file_path):

    # Load Dataset
    df = pd.read_csv("data/AirQualityUCI.csv",
        sep=";",
        decimal=","
    )

    # Keep useful columns
    df = df[
        ["Date", "Time", "CO(GT)", "NO2(GT)"]
    ]

    # Remove invalid values
    df = df[
        (df["CO(GT)"] != -200) &
        (df["NO2(GT)"] != -200)
    ]

    # Create AQI Friction
    df["AQI_Friction"] = (
        (df["CO(GT)"] * 20)
        +
        (df["NO2(GT)"] * 0.5)
    )

    # Normalize to 0-100
    scaler = MinMaxScaler()

    df["AQIScore"] = scaler.fit_transform(
        df[["AQI_Friction"]]
    ) * 100

    # Create Zones
    df = create_zones(df)

    # Generate Zone Scores
    zone_df = generate_zone_scores(df)

    zone_df.to_csv(
        "outputs/aqi_scores.csv",
        index=False
    )

    return zone_df
def create_zones(df):

    zone_size = len(df) // 5

    zones = []

    for i in range(len(df)):

        if i < zone_size:
            zones.append("Kothrud")

        elif i < zone_size * 2:
            zones.append("Baner")

        elif i < zone_size * 3:
            zones.append("Wakad")

        elif i < zone_size * 4:
            zones.append("Hadapsar")

        else:
            zones.append("Shivajinagar")

    df["Zone"] = zones

    return df

def generate_zone_scores(df):

    zone_df = (
        df.groupby("Zone")["AQIScore"]
        .mean()
        .reset_index()
    )

    return zone_df