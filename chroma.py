import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None, duration=10)  # Load 10 seconds of audio

chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

chromagram_mean = chromagram.mean(axis=1)

result = sum(chromagram_mean)/len(chromagram_mean)
print(result)
