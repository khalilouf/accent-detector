# 🗣️ English Accent Detector

This project is a web-based application that detects the **English accent** (e.g., American, British, Australian) of a speaker from a publicly available video URL (e.g., YouTube). It uses audio processing, a deep learning model, and a Streamlit interface.

![screenshot](https://your-screenshot-link-if-any.png)

---

## 🚀 Features

- 🔗 Input a public video URL
- 🎞️ Automatically download the video
- 🔊 Extract and convert audio
- 🧠 Run accent detection using a pre-trained model
- 📊 Display the detected accent and confidence score

---

## 📦 Dependencies

All Python dependencies are listed in `requirements.txt`. Key ones include:

- `streamlit`
- `pydub`
- `moviepy`
- `torch`, `torchaudio`, `transformers`
- `ffmpeg-python`
- `audioop-lts` ✅ (workaround for Python 3.13 compatibility)

System-level packages required (listed in `packages.txt` for Streamlit Cloud):

- `ffmpeg`

---

## 🛠️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/khalilouf/accent-detector.git
cd accent-detector
2. Create a virtual environment
bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
bash
Copier
Modifier
pip install -r requirements.txt
4. Run the app
bash
Copier
Modifier
streamlit run streamlit_app.py
☁️ Deploying on Streamlit Cloud
Ensure the following files are present:

requirements.txt ✅

runtime.txt (Python version):

Copier
Modifier
python-3.12.3
packages.txt (system packages):

nginx
Copier
Modifier
ffmpeg
Deployment Steps
Push your code to GitHub

Go to Streamlit Cloud

Connect your GitHub repository

Set streamlit_app.py as the entry point

Done! 🚀

📁 Project Structure
bash
Copier
Modifier
accent-detector/
├── streamlit_app.py          # Main app interface
├── requirements.txt
├── runtime.txt
├── packages.txt
├── .gitignore
├── utils/
│   ├── downloader.py         # Handles video downloading
│   ├── audio_extractor.py    # Extracts and converts audio
│   └── accent_classifier.py  # Loads model and predicts accent
├── output/                   # Temporary folder for audio files
└── downloads/                # Temporary folder for downloaded videos
📌 Notes
This app is intended for educational and demonstration purposes.

The accuracy of the accent classifier may vary and can be improved with fine-tuning.

Ensure the input video URLs are publicly accessible.

🤝 Contributions
Contributions are welcome! Please fork the repository and submit a pull request.

🧑‍💻 Author
Khalil Trabelsi
LinkedIn • GitHub

📄 License
This project is licensed under the MIT License – feel free to use, modify, and share!

yaml
Copier
Modifier

---

Let me know if you want to:
- Add a real screenshot or demo GIF
- Include an example video URL
- Auto-generate and save this as `README.md` in your repo

Would you like me to generate and upload the final `README.md` file for you?