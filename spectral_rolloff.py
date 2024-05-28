import numpy as np
import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Calculate the spectral roll-off
spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)

# Calculate the mean spectral roll-off value
mean_spectral_rolloff = np.mean(spectral_rolloff)

print("Mean Spectral Roll-off:", mean_spectral_rolloff)
