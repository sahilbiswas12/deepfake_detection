import cv2
import numpy as np
from tensorflow.keras.models import load_model

def preprocess_frame(frame, img_size=(224, 224)):
    """
    Preprocess a video frame to prepare it for model prediction.
    
    Args:
    - frame (ndarray): The video frame to preprocess.
    - img_size (tuple): Target size for resizing the frame.
    
    Returns:
    - ndarray: Preprocessed frame suitable for model input.
    """
    # Resize the frame
    resized_frame = cv2.resize(frame, img_size)
    # Normalize the frame
    normalized_frame = resized_frame / 255.0
    # Expand dimensions to match model input shape
    return np.expand_dims(normalized_frame, axis=0)

def predict_video(video_path, model_path, threshold=0.5, img_size=(224, 224)):
    """
    Predict whether a video is real or fake using a trained model.
    
    Args:
    - video_path (str): Path to the video file.
    - model_path (str): Path to the trained model (.h5 file).
    - threshold (float): Probability threshold to classify frames as fake.
    - img_size (tuple): Target size for resizing video frames.
    
    Returns:
    - str: Result indicating whether the video is real or fake.
    """
    # Load the trained model
    model = load_model(model_path)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return "Error: Could not open video file."

    frame_count = 0
    fake_frames = 0

    # Process the video frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:  # If no more frames, break
            break

        frame_count += 1

        # Preprocess the frame
        preprocessed_frame = preprocess_frame(frame, img_size)

        # Make prediction
        prediction = model.predict(preprocessed_frame)

        # Check if the frame is predicted as fake
        if prediction[0][0] > threshold:
            fake_frames += 1

    cap.release()

    # Calculate the percentage of fake frames
    fake_percentage = (fake_frames / frame_count) * 100
    result = "The video is predicted to be FAKE." if fake_percentage > 50 else "The video is predicted to be REAL."
    
    return result

