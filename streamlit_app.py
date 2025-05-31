import streamlit as st
from utils.downloader import download_video
from utils.audio_extractor import extract_audio
from utils.accent_classifier import load_model, predict_accent

st.title("🎙️ English Accent Detector")

st.markdown("""
This tool extracts audio from a public video URL and detects the speaker's English accent (American, British, or Australian).
""")

url = st.text_input("Enter a YouTube video URL")

if st.button("Analyze"):
    if url:
        with st.spinner("Downloading and processing..."):
            try:
                video_path = download_video(url)
                audio_path = extract_audio(video_path)
                model, processor = load_model()
                accent, confidence = predict_accent(audio_path, model, processor)
                st.success(f"🗣️ Detected Accent: **{accent.capitalize()}**")
                st.info(f"Confidence Score: **{confidence}%**")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

