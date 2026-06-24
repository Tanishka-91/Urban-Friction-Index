from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("outputs/final_ufi.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/ufi")
def api_ufi():

    data = []

    for _, row in df.iterrows():

        data.append({
            "zone": row["Zone"],
            "ufi": round(row["UFI"], 2),

            "breakdown": {
                "traffic": {
                    "score": round(row["TrafficScore"], 2)
                },

                "air_quality": {
                    "score": round(row["AQIScore"], 2)
                },

                "transit": {
                    "score": round(row["TransportScore"], 2)
                },

                "complaints": {
                    "score": round(row["RoadScore"], 2),
                    "complaint_count": int(row["RoadScore"])
                },

                "noise": {
                    "score": 20
                },

                "crowd": {
                    "score": 30
                }
            },

            "prediction": {
                "predicted_ufi": round(row["UFI"] + 5, 2),
                "trend": "Increasing",
                "trend_icon": "↑",
                "trend_color": "#ef4444",
                "day": "Tomorrow"
            }
        })

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
from flask import request, jsonify

@app.route("/api/complaint", methods=["POST"])
def api_complaint():

    data = request.get_json()

    zone = data["zone"]
    category = data["category"]

    print(
        f"Complaint received: {zone} - {category}"
    )

    return jsonify({
        "status": "success"
    })