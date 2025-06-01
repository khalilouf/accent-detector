import streamlit as st
from utils.downloader import download_video
from utils.audio_extractor import extract_audio
from utils.accent_classifier import load_model, predict_accent

st.set_page_config(page_title="Accent Detector", page_icon="🗣️")
st.title("🎙️ English Accent Detector")

url = st.text_input("Enter a public video URL (e.g., YouTube)")

if url:
    with st.spinner("Downloading video..."):
        video_path = download_video(url)

    with st.spinner("Extracting audio..."):
        audio_path = extract_audio(video_path)

    with st.spinner("Loading model and predicting..."):
        model, processor = load_model()
        accent, confidence = predict_accent(audio_path, model, processor)

    st.success(f"🗣️ Detected Accent: **{accent.capitalize()}**")
    st.info(f"Confidence: {confidence:.2f}%")
