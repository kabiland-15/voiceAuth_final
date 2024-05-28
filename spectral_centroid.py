import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None)

# Compute the spectral centroid
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

# Calculate the mean of the spectral centroid values
mean_spectral_centroid = spectral_centroid.mean()

print("Mean Spectral Centroid:", mean_spectral_centroid)
