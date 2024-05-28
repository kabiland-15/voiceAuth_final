Deep Fake Voice Detection Using CRNN and Machine Learning Models
Project Overview
This project aims to develop a robust system for detecting deep fake voices using Convolutional Recurrent Neural Networks (CRNN) and traditional machine learning algorithms such as Random Forest Classifier and XGBoost. The system leverages audio feature extraction techniques provided by the librosa and numpy libraries to process and analyze audio data. The dataset utilized for training and evaluation is sourced from the Deepfake Detection Challenge on Kaggle.

Table of Contents
Introduction
Features
Dataset
Installation
Usage
Model Architecture
Results
Contributing
License
Acknowledgements
Introduction
The proliferation of deep fake technology poses significant challenges, especially in the realm of audio. This project addresses these challenges by developing a detection system capable of distinguishing between real and fake audio samples. Utilizing advanced machine learning techniques and deep learning models, the project aims to achieve high accuracy and robustness in detecting manipulated audio.

Features
Audio Feature Extraction: Utilizes librosa and numpy for comprehensive audio feature extraction, including Mel-frequency cepstral coefficients (MFCCs), chroma features, and spectral contrast.
Machine Learning Models: Implements Random Forest Classifier and XGBoost for classification tasks.
Deep Learning Model: Employs Convolutional Recurrent Neural Networks (CRNN) for deep learning-based detection.
Performance Evaluation: Comprehensive performance evaluation using metrics such as accuracy, precision, recall, and F1-score.
Dataset
The dataset used in this project is obtained from the Deepfake Detection Challenge on Kaggle. It includes a variety of audio samples labeled as real or fake, providing a robust foundation for training and evaluation.

Installation
To set up the project locally, follow these steps:

Clone the repository:

git clone https://github.com/kabiland-15/voiceAuth_final.git
cd deepfake-voice-detection

Model Architecture
CRNN (Convolutional Recurrent Neural Network)
The CRNN model combines convolutional layers for feature extraction with recurrent layers (LSTM/GRU) for sequential data processing. This architecture is particularly effective for audio data due to its ability to capture both spatial and temporal features.

Machine Learning Models
Random Forest Classifier: An ensemble learning method based on constructing multiple decision trees.
XGBoost: An optimized gradient boosting algorithm that is highly efficient and scalable.
Results
The performance of each model is evaluated using standard metrics. Detailed results and analysis are available in the results/ directory, including accuracy, precision, recall, and F1-score for each model.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Fork the project
Create your feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/YourFeature)
Open a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The dataset used in this project is from the Deepfake Detection Challenge on Kaggle.
The librosa library for audio analysis.
The contributors and maintainers of the numpy library.
The open-source community for providing tools and libraries that make this project possible.
