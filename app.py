import streamlit as st
import json
import os

# Function to load recipes
def load_recipes(meal_type):
    file_path = f"recipes/{meal_type}.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Page setup
st.set_page_config(page_title="Recipes & Meals", layout="wide")
st.title("🍽️ Recipes & Meals")
st.sidebar.title("Meal Type")
meal_type = st.sidebar.selectbox("Choose a meal", ["breakfast", "lunch", "dinner"])

# Search bar
search_query = st.sidebar.text_input("Search Recipes")

# Load recipes
recipes = load_recipes(meal_type)

# Filter recipes
if search_query:
    recipes = [r for r in recipes if search_query.lower() in r['name'].lower()]

# Display recipes
if recipes:
    for recipe in recipes:
        st.subheader(recipe['name'])
        st.image(recipe['image'], width=300)
        st.markdown("**Ingredients:**")
        st.write(", ".join(recipe['ingredients']))
        st.markdown("**Instructions:**")
        st.write(recipe['instructions'])
        st.markdown("---")
else:
    st.warning("No recipes found.")
