import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def process_road(file_path):

    df = pd.read_csv("data/road_complaints.csv")

    # Calculate total road issue score
    df["RoadIssue"] = (
        df["Potholes"] +
        df["RoadCracks"] +
        df["Waterlogging"] +
        df["Complaints"]
    )

    scaler = MinMaxScaler()

    df["RoadScore"] = scaler.fit_transform(
        df[["RoadIssue"]]
    ) * 100

    road_scores = df[["Zone", "RoadScore"]]

    road_scores.to_csv(
        "outputs/road_scores.csv",
        index=False
    )

    return road_scores
