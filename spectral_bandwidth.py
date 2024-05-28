import numpy as np
import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Calculate the spectral bandwidth
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)

# Calculate the mean spectral bandwidth value
mean_spectral_bandwidth = np.mean(spectral_bandwidth)

print("Mean Spectral Bandwidth:", mean_spectral_bandwidth)
