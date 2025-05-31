import argparse
from utils.downloader import download_video
from utils.audio_extractor import extract_audio
from utils.accent_classifier import load_model, predict_accent

def main(url):
    print("[1] Downloading video...")
    video_path = download_video(url)

    print("[2] Extracting audio...")
    audio_path = extract_audio(video_path)

    print("[3] Loading model and processor...")
    model, processor = load_model()

    print("[4] Predicting accent...")
    accent, confidence = predict_accent(audio_path, model, processor)

    print(f"\n🗣️ Detected Accent: {accent.capitalize()} (Confidence: {confidence}%)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="English Accent Detection from a Video URL")
    parser.add_argument("url", type=str, help="Public URL of the video (e.g., YouTube link)")
    args = parser.parse_args()
    main(args.url)
