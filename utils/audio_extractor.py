import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def extract_audio(video_path, output_path="output/audio.wav"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clip = VideoFileClip(video_path)
    audio_path = output_path.replace(".wav", ".mp3")
    clip.audio.write_audiofile(audio_path, codec='libmp3lame', verbose=False, logger=None)

    # Convert mp3 to wav (16kHz mono)
    audio = AudioSegment.from_mp3(audio_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_path, format="wav")

    return output_path
