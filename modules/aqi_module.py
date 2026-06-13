import pandas as pd

# Load Air Quality Dataset
df = pd.read_csv(
    "air_quality/AirQualityUCI.csv",
    sep=";",
    decimal=","
)

# Select useful columns
df = df[["Date", "Time", "CO(GT)", "NO2(GT)"]]

# Remove missing values (-200)
df = df[
    (df["CO(GT)"] != -200) &
    (df["NO2(GT)"] != -200)
]

# Create AQI Friction Score
df["AQI_Friction"] = (
    (df["CO(GT)"] * 20) +
    (df["NO2(GT)"] * 0.5)
)

# Display first 5 rows
print("\nFirst 5 Records:\n")
print(df.head())

# Display summary
print("\nTotal Records:", len(df))
print("Average AQI Friction:", round(df["AQI_Friction"].mean(), 2))

# Save cleaned dataset
df.to_csv(
    "air_quality/aqi_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")