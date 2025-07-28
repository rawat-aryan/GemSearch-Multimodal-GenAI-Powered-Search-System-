import streamlit as st
import requests

st.set_page_config(page_title="GemSearch", layout="centered")
st.title("🔍 GemSearch: GenAI-Powered Multimodal Search")

option = st.selectbox("Choose input type:", ("Text", "Image", "Audio"))

# ---------------------- TEXT SEARCH ----------------------
if option == "Text":
    query = st.text_input("Enter your text query:")

    if st.button("Search", key="text_btn") and query:
        try:
            res = requests.post("http://localhost:8000/search_text", json={"query": query})
            if res.status_code == 200:
                st.success("Search completed ✅")
                st.json(res.json())
            else:
                st.error(f"❌ Error: {res.status_code}")
                st.text(res.text)
        except Exception as e:
            st.error(f"Request failed: {e}")

# ---------------------- IMAGE SEARCH ----------------------
elif option == "Image":
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if st.button("Search", key="image_btn") and file:
        try:
            res = requests.post("http://localhost:8000/search_image", files={"file": file})
            if res.status_code == 200:
                st.success("Image search completed ✅")
                st.json(res.json())
            else:
                st.error(f"❌ Error: {res.status_code}")
                st.text(res.text)
        except Exception as e:
            st.error(f"Request failed: {e}")

# ---------------------- AUDIO SEARCH ----------------------
elif option == "Audio":
    file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

    if st.button("Search", key="audio_btn") and file:
        try:
            res = requests.post("http://localhost:8000/search_audio", files={"file": file})
            if res.status_code == 200:
                st.success("Audio search & transcription completed ✅")
                result = res.json()
                st.subheader("🎤 Transcript:")
                st.write(result["transcript"])
                st.subheader("🔍 Text Search Results:")
                st.json(result["search"])
            else:
                st.error(f"❌ Error: {res.status_code}")
                st.text(res.text)
        except Exception as e:
            st.error(f"Request failed: {e}")
