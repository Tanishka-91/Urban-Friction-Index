from modules.traffic_module import process_traffic
import matplotlib.pyplot as plt

traffic_df = process_traffic("data/traffic.csv")

print(traffic_df)

traffic_df.plot(
    x="Zone",
    y="TrafficScore",
    kind="bar",
    color="skyblue",
    legend=False
)

plt.title("Zone-wise Traffic Score")
plt.ylabel("Traffic Score")
plt.show()