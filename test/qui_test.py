import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from modules.AQI1 import process_aqi

aqi_df = process_aqi(
    "data/AirQualityUCI.csv"
)

print(aqi_df)