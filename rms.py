import numpy as np
import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Calculate the Root Mean Square (RMS) value
rms = np.sqrt(np.mean(y**2))

print("Root Mean Square (RMS) value:", rms)
