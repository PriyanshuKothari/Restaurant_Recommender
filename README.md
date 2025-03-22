# 🍽️ Restaurant Recommender System

## 📌 Overview
This is an **AI-powered restaurant recommendation system** that suggests personalized restaurants based on:

✅ **Collaborative Filtering (User-Based Recommendations)** – Suggests restaurants liked by similar users.  
✅ **Content-Based Filtering (Cuisine Similarity)** – Finds restaurants with similar cuisines.  
✅ **Hybrid Model** – Combines both approaches for better accuracy.  

Built using **Flask, scikit-surprise, scikit-learn, and Pandas**.  

---

## 🛠️ Features
✅ **Personalized recommendations** based on user preferences.  
✅ **Real-time API** to get restaurant recommendations.  
✅ **Interactive web interface** for easy access.  
✅ **Hybrid AI model** for better accuracy.  

---

## 📂 Project Structure

    📂 restaurant-recommender
     ├── 📂 static/          # CSS files
     ├── 📂 templates/       # HTML templates
     ├── recommender.py      # AI model (converted from Jupyter)
     ├── app.py             # Flask backend
     ├── requirements.txt   # Required libraries
     ├── README.md          # Project documentation


---

## 🚀 Installation & Setup

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Priyanshukothari/Restaurant_Recommender.git
cd Restaurant_Recommender

```
### 🔹 2. Install Dependencies
```bash
pip install -r requirements.txt

```
### 🔹 3. Run the Flask App
```bash
python app.py
```
### 🔹 4. Access the Web Interface
Open your browser and go to:
```bash
http://127.0.0.1:5000/
```
## 📌 Usage
1. **Enter User ID** (e.g., `U1077`).  
2. **Enter a Restaurant Name** (e.g., `"Tortas Locas Hipocampo"`).  
3. **Enter Your City** (e.g., `"San Luis Potosi"`).  
4. **Click "Get Recommendations"** to view personalized results. 

## 🌟 API Endpoints
This project also provides an API for external applications.

| **Endpoint**   | **Method** | **Description** |
|---------------|------------|----------------|
| `/recommend`  | **GET**    | Get restaurant recommendations |
### 🔹 Example API Request
```bash
http://127.0.0.1:5000/recommend?user_id=U1077&restaurant_name=Tortas%20Locas%20Hipocampo&user_city=San%20Luis%20Potosi
```

## ✅ Response Format (JSON)
```bash
[
    {
        "name": "Restaurant la Chalita",
        "Rcuisine_y": "Mexican",
        "city": "San Luis Potosi"
    },
    {
        "name": "Restaurante Marisco Sam",
        "Rcuisine_y": "Mexican",
        "city": "San Luis Potosi"
    }
]
```

## 📦 Dependencies (requirements.txt)
```bash
Flask
pandas
numpy
scikit-learn
scikit-surprise
```

## 📌 Future Improvements
- 🚀 **Add Sentiment Analysis** to filter restaurants based on reviews.  
- 🚀 **Deploy API** to **Render/Heroku** for global access.  
- 🚀 **Improve UI** for a better user experience. 

## 💡 Contributors
- 👤 Priyanshu Kothari
- GitHub: Priyanshukothari

## 📜 License
This project is open-source under the MIT License.

