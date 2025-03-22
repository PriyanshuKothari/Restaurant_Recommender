#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
# Load datasets (Update file paths if needed)
df_ratings = pd.read_csv("restaurant_data/rating_final.csv")
df_restaurants = pd.read_csv("restaurant_data/geoplaces2.csv", encoding="ISO-8859-1")  # Restaurant details
df_user_cuisine = pd.read_csv("restaurant_data/usercuisine.csv")  # User preferences
df_restaurant_cuisine = pd.read_csv("restaurant_data/chefmozcuisine.csv")  # Restaurant cuisine types


# In[3]:


# Merge ratings with restaurant details (name, location, etc.)
df_merged = df_ratings.merge(df_restaurants[['placeID', 'name', 'city', 'state', 'price']], on='placeID', how='left')


# In[4]:


# Merge with restaurant cuisine details
df_merged = df_merged.merge(df_restaurant_cuisine, on='placeID', how='left')


# In[5]:


# Merge with user cuisine preferences
df_merged = df_merged.merge(df_user_cuisine, on='userID', how='left')


# In[6]:


# Display the final merged dataset
print(df_merged.head())


# In[8]:


import os
os.system('pip install scikit-surprise')




# In[11]:


from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split


# In[12]:


# Define rating scale (0-2 as per dataset)
reader = Reader(rating_scale=(0, 2))


# In[13]:


# Load merged data into Surprise format
data = Dataset.load_from_df(df_merged[['userID', 'placeID', 'rating']], reader)


# In[14]:


train, test = train_test_split(data, test_size= 0.2)


# In[15]:


# Train SVD model
model = SVD()
model.fit(train)


# In[16]:


# Test model accuracy
from surprise.accuracy import rmse
predictions = model.test(test)
print("Model RMSE:", rmse(predictions))


# In[19]:


def get_collaborative_recommendations(user_id, num_recommendations=5):
    # Get all unique restaurant IDs
    all_restaurants = df_merged['placeID'].unique()
    
    # Predict ratings for all restaurants
    predictions = [model.predict(user_id, restaurant) for restaurant in all_restaurants]
    
    # Sort predictions by estimated rating (descending order)
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    # Get top recommended restaurant IDs
    top_recommendations = [pred.iid for pred in predictions[:num_recommendations]]
    
    # Get restaurant details for recommendations
    return df_merged[df_merged['placeID'].isin(top_recommendations)][['name', 'Rcuisine_y', 'city']].drop_duplicates()


# In[20]:


get_collaborative_recommendations("U1077")  # Replace with any user ID


# In[23]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[24]:


# Fill missing cuisine values with an empty string
df_merged['Rcuisine_y'].fillna('', inplace=True)

# Convert cuisine type into a single string for each restaurant
df_merged['cuisine_combined'] = df_merged['Rcuisine_y']

# Apply TF-IDF Vectorization on cuisine types
vectorizer = TfidfVectorizer()
cuisine_matrix = vectorizer.fit_transform(df_merged['cuisine_combined'])

# Compute Cosine Similarity between restaurants based on cuisine type
cosine_sim = cosine_similarity(cuisine_matrix, cuisine_matrix)


# In[25]:


def recommend_similar_restaurants_location_based(restaurant_name, user_city, num_recommendations=5):
    # Find the restaurant index
    idx = df_merged[(df_merged['name'] == restaurant_name) & (df_merged['city'] == user_city)].index
    
    if len(idx) == 0:
        return "Restaurant not found in database for this city."
    
    idx = idx[0]
    
    # Get similarity scores for the restaurant
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort restaurants by similarity score (descending)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get indices of top similar restaurants
    similar_indices = [i[0] for i in sim_scores[1:num_recommendations*2]]  # Get more recommendations first
    
    # Filter recommendations by the same city
    recommended_restaurants = df_merged.iloc[similar_indices][['name', 'Rcuisine_y', 'city']].drop_duplicates()
    recommended_restaurants = recommended_restaurants[recommended_restaurants['city'] == user_city].head(num_recommendations)
    
    return recommended_restaurants


# In[26]:


def hybrid_recommendations(user_id, restaurant_name, user_city, num_recommendations=5):
    # Get collaborative filtering recommendations
    collab_recs = get_collaborative_recommendations(user_id, num_recommendations)
    
    # Get content-based recommendations
    content_recs = recommend_similar_restaurants_location_based(restaurant_name, user_city, num_recommendations)
    
    # Merge results (removing duplicates)
    hybrid_results = pd.concat([collab_recs, content_recs]).drop_duplicates().head(num_recommendations)
    
    return hybrid_results


# In[27]:


hybrid_recommendations("U1077", "Tortas Locas Hipocampo", "San Luis Potosi")


# In[ ]:




