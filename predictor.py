import pandas as pd
import joblib

def predict_voice(input_data):
    model_path = r"D:\projects\voiceAuth_final\rfc_model.pkl"
    model = joblib.load(model_path)
    input_df = pd.DataFrame([input_data])
    return model.predict(input_df)[0]
