from features import FeatureExtractor
from predictor import predict_voice

audio_file_path = '1.wav'
feature_extractor = FeatureExtractor(audio_file_path)
features = feature_extractor.extract_features()
print(features)

print(predict_voice(features))
