# Import necessary libraries
import streamlit as st
from fuzzywuzzy import process

# Define your array of items
array_of_items = ["USA", "UK", "Canada", "Australia", "Germany", "France", "India", "Greece", "Bhutan", "South Korea", "Japan", "Russia", "China","Italy","Brazil","South Africa","New Zealand","Saudi Arabia"]

def find_closest_match(input_text, array_of_items):
    closest_match, similarity_score = process.extractOne(input_text, array_of_items)
    return closest_match, similarity_score

# Streamlit app
st.title("Closest Match Finder")

input_text = st.text_input("Enter text:")
if input_text:
    closest_match, similarity_score = find_closest_match(input_text, array_of_items)
    st.write("Closest Match:", closest_match)
    st.write("Similarity Score:", similarity_score)
