from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load models
claim_model = pickle.load(open("claim_model.pkl", "rb"))
fraud_model = pickle.load(open("fraud_model.pkl", "rb"))

# -----------------------------------
@app.route("/")
def home():
    return render_template("home.html")

# -----------------------------------
@app.route("/app")
def app_page():
    return render_template("combined.html")

# -----------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    task = request.form["task"]

    data = request.form.to_dict()
    data.pop("task")

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    if task == "claim":
        df = df.reindex(columns=claim_model.feature_names_in_, fill_value=0)
        prediction = claim_model.predict(df)[0]
        result = f"💰 Estimated Claim: ₹ {round(prediction, 2)}"

    else:
        df = df.reindex(columns=fraud_model.feature_names_in_, fill_value=0)
        pred = fraud_model.predict(df)[0]
        result = "🚨 Fraud Detected" if pred == 1 else "✅ Not Fraud"

    return render_template("result.html", result=result)

# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)
