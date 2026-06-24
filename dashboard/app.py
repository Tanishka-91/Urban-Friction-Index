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
"""
app.py (v2 — upgraded with ML prediction + 6 factors + new routes)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from flask import Flask, jsonify, render_template, request
from modules import friction_engine, road_module
from modules.ml_predictor import predict_all_zones

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ufi")
def api_ufi():
    data = friction_engine.get_all_zones_ufi()
    # attach ML predictions
    zone_scores = {z["zone"]: z["ufi"] for z in data}
    predictions = {p["zone"]: p for p in predict_all_zones(zone_scores)}
    for z in data:
        z["prediction"] = predictions.get(z["zone"], {})
    return jsonify(data)

@app.route("/api/ufi/<zone>")
def api_ufi_zone(zone):
    return jsonify(friction_engine.calculate_ufi(zone))

@app.route("/api/complaint", methods=["POST"])
def api_complaint():
    payload = request.get_json()
    zone = payload.get("zone")
    category = payload.get("category", "general")
    if not zone:
        return jsonify({"error": "zone is required"}), 400
    road_module.add_complaint(zone, category)
    return jsonify({"status": "ok", "zone": zone, "category": category})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
