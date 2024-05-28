import numpy as np
import librosa

class FeatureExtractor:
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.y, self.sr = librosa.load(audio_file_path, sr=None)

    def calculate_zero_crossing_rate(self):
        zero_crossing_rate = librosa.feature.zero_crossing_rate(self.y)
        return np.mean(zero_crossing_rate)

    def calculate_spectral_rolloff(self):
        spectral_rolloff = librosa.feature.spectral_rolloff(y=self.y, sr=self.sr)
        return np.mean(spectral_rolloff)

    def calculate_spectral_centroid(self):
        spectral_centroid = librosa.feature.spectral_centroid(y=self.y, sr=self.sr)
        return np.mean(spectral_centroid)

    def calculate_spectral_bandwidth(self):
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=self.y, sr=self.sr)
        return np.mean(spectral_bandwidth)

    def calculate_rms(self):
        return np.sqrt(np.mean(self.y**2))

    def calculate_mfccs(self):
        mfccs = librosa.feature.mfcc(y=self.y, sr=self.sr, n_mfcc=20)
        return np.mean(mfccs, axis=1)

    def calculate_chromagram_mean(self):
        chromagram = librosa.feature.chroma_stft(y=self.y, sr=self.sr)
        chromagram_mean = chromagram.mean(axis=1)
        return np.mean(chromagram_mean)

    def extract_features(self):
        features = []
        features.append(self.calculate_chromagram_mean())
        features.append(self.calculate_rms())
        features.append(self.calculate_spectral_centroid())
        features.append(self.calculate_spectral_bandwidth())
        features.append(self.calculate_spectral_rolloff())
        features.append(self.calculate_zero_crossing_rate())
        features.extend(self.calculate_mfccs())

        return features
