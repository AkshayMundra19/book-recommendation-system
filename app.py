import streamlit as st
import sys

sys.path.append("src")

from data_preprocessing import load_dataset
from recommendation import recommend_books

st.set_page_config(page_title="AI Book Recommendation System")

st.title(" AI Book Recommendation System")

df = load_dataset()

st.header("Choose Your Preferences")

language = st.selectbox(
    "Select Book Language",
    ["English", "Hindi"]
)

genres = sorted(df["genre"].unique())

genre = st.selectbox(
    "Select Your Interest",
    genres
)

if st.button("Recommend Books"):

    books = recommend_books(df, language, genre)

    st.subheader(" Recommended Books")

    if books:
        for book in books:
            st.write(" ", book)
    else:
        st.warning("No books found for this category.")