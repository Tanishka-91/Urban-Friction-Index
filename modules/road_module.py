import pandas as pd

# Load road complaints dataset
df = pd.read_csv("data/road_complaints.csv")

# Severity weights
severity_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

# Convert severity to weight
df["Severity_Weight"] = df["Severity"].map(severity_map)

# Calculate Road Friction Score
df["Road_Friction"] = df["Complaints"] * df["Severity_Weight"]

print(df)

print("\nAverage Road Friction:", round(df["Road_Friction"].mean(), 2))

# Save cleaned dataset
df.to_csv("data/road_cleaned.csv", index=False)

print("\nRoad cleaned dataset saved successfully!")