
import streamlit as st
import requests

st.title("GemSearch: GenAI Search System")

option = st.selectbox("Choose input type", ("Text", "Image", "Audio"))

if option == "Text":
    query = st.text_input("Enter your query:")
    if st.button("Search"):
        res = requests.post("http://localhost:8000/search_text", params={"query": query})
        st.json(res.json())

elif option == "Image":
    file = st.file_uploader("Upload image", type=["jpg", "png"])
    if st.button("Search") and file:
        res = requests.post("http://localhost:8000/search_image", files={"file": file})
        st.json(res.json())

elif option == "Audio":
    file = st.file_uploader("Upload audio", type=["wav", "mp3"])
    if st.button("Search") and file:
        res = requests.post("http://localhost:8000/search_audio", files={"file": file})
        st.json(res.json())
