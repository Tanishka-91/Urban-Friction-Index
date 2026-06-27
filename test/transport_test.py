import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from modules.transport_module import process_transport

transport_df = process_transport(
    "data/transport_data.csv"
)

print(transport_df)
import matplotlib.pyplot as plt

transport_df.plot(
    x="Zone",
    y="TransportScore",
    kind="bar",
    color="green",
    legend=False
)

plt.title("Zone-wise Transport Score")
plt.ylabel("Transport Score")

plt.show()