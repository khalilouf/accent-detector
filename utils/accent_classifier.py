import torch
import torch.nn as nn
from transformers import Wav2Vec2Model, Wav2Vec2Processor
import torchaudio

LABEL_MAP = {0: "american", 1: "british", 2: "australian"}

class AccentClassifier(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")
        self.classifier = nn.Linear(self.backbone.config.hidden_size, num_classes)

    def forward(self, input_values, attention_mask=None):
        outputs = self.backbone(input_values, attention_mask=attention_mask)
        hidden_states = outputs.last_hidden_state
        pooled = hidden_states.mean(dim=1)
        return self.classifier(pooled)

def load_model():
    model = AccentClassifier(num_classes=len(LABEL_MAP))
    # model.load_state_dict(torch.load("model.pt")) ← à ajouter si tu as entraîné un modèle
    model.eval()
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    return model, processor

def preprocess_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
    return waveform.squeeze()

def predict_accent(file_path, model, processor):
    waveform = preprocess_audio(file_path)
    inputs = processor(waveform, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs)
        probs = torch.nn.functional.softmax(logits, dim=-1)
        pred = torch.argmax(probs, dim=-1).item()
        confidence = probs[0, pred].item()
    return LABEL_MAP[pred], round(confidence * 100, 2)
