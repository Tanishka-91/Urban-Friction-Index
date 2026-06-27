import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def process_transport(file_path):

    df = pd.read_csv("data/transport_data.csv")

    # Create Transport Issue Score
    df["TransportIssue"] = (
        df["BusDelay"]
        + df["CancelledTrips"]
        + df["MissedTrips"]
    )

    scaler = MinMaxScaler()

    df["TransportScore"] = scaler.fit_transform(
        df[["TransportIssue"]]
    ) * 80

    transport_scores = df[
        ["Zone", "TransportScore"]
    ]

    transport_scores.to_csv(
        "outputs/transport_scores.csv",
        index=False
    )

    return transport_scores