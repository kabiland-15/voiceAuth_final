import numpy as np
import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Calculate the zero-crossing rate
zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

# Calculate the mean zero-crossing rate value
mean_zero_crossing_rate = np.mean(zero_crossing_rate)

print("Mean Zero Crossing Rate:", mean_zero_crossing_rate)
