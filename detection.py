import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, LSTM, Dense, TimeDistributed, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def predict_face_swap(folder_path):
  # Image dimensions
  img_width, img_height = 128, 128

  # CNN model for feature extraction
  cnn_model = Sequential()
  cnn_model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
  cnn_model.add(MaxPooling2D((2, 2)))
  cnn_model.add(MaxPooling2D((2, 2)))
  cnn_model.add(Flatten())

  # RNN/LSTM model for sequence analysis
  model = Sequential()
  model.add(TimeDistributed(cnn_model, input_shape=(None, img_width, img_height, 3)))
  model.add(LSTM(64, return_sequences=False))
  model.add(Dropout(0.5))
  model.add(Dense(1, activation='sigmoid'))

  # Load pre-trained weights (replace with your actual weights file)
  model.load_weights('my_model.keras')

  # Data generator for loading frames
  datagen = ImageDataGenerator(rescale=1./255)
  frames_generator = datagen.flow_from_directory(
      folder_path,
      target_size=(img_width, img_height),
      batch_size=1,  # Process frames one by one
      class_mode=None,  # We don't need labels for prediction
      shuffle=False  # Maintain frame order
  )

  # Predict on the frames
  predictions = model.predict(frames_generator)

  # Analyze predictions (e.g., average or threshold-based)
  average_prediction = predictions.mean()
  if average_prediction > 0.5:
    print("Fake video (face swap detected)")
  else:
    print("Real video")

# Get folder path from user input
folder_path = input("Enter the path to the folder containing frames: ")
predict_face_swap(folder_path)



