import torchaudio

print("Torchaudio version:", torchaudio.__version__)
waveform, sample_rate = torchaudio.load("test.wav")  # Remplace par un petit fichier audio local
print("Loaded waveform shape:", waveform.shape)
