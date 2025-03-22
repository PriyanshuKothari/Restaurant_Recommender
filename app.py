from flask import Flask, request, jsonify, render_template
import pandas as pd
from recommender import hybrid_recommendations  # Import from recommender.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get("user_id")
    restaurant_name = request.args.get("restaurant_name")
    user_city = request.args.get("user_city")

    if not user_id or not restaurant_name or not user_city:
        return jsonify({"error": "Missing parameters! Provide user_id, restaurant_name, and user_city."}), 400

    # Get recommendations
    recommendations = hybrid_recommendations(user_id, restaurant_name, user_city)

    # Convert DataFrame to JSON
    result = recommendations.to_dict(orient="records")

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
