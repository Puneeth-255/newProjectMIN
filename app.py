from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

# Load trained model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        result = model.predict([features])[0]

        prediction = "⚠️ Phishing Website" if result == 1 else "✅ Legitimate Website"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
