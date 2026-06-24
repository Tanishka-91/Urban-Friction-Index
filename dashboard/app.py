from flask import Flask, render_template
import pandas as pd

import os
import pandas as pd

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# csv_path = os.path.join(
#     BASE_DIR,
#     "outputs",
#     "final_ufi.csv"
# )

# df = pd.read_csv(csv_path)

app = Flask(__name__)

df = pd.read_csv("URBAN-FRICTION-INDEX/outputs/final_ufi.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():

    zones = df["Zone"].tolist()
    ufi = df["UFI"].tolist()

    return render_template(
        "dashboard.html",
        zones=zones,
        ufi=ufi
    )


@app.route("/zones")
def zones():

    data = df.to_dict(
        orient="records"
    )

    return render_template(
        "zones.html",
        data=data
    )


@app.route("/recommendations")
def recommendations():

    data = df.to_dict(
        orient="records"
    )

    return render_template(
        "recommendations.html",
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)