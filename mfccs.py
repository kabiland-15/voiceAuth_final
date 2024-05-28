import numpy as np
import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Calculate the MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

# Calculate the mean of each MFCC coefficient
mean_mfccs = np.mean(mfccs, axis=1)

print("Mean MFCCs values (from 1 to 20):", mean_mfccs)
