def predict_deepfake(frames, model, threshold=0.5):
    # Perform predictions
    predictions = model.predict(frames)
    # Output results
    for idx, prediction in enumerate(predictions):
        print(f"Frame {idx}: Real probability: {prediction[0]:.2f}, Fake probability: {prediction[1]:.2f}")

    # Aggregate results
    fake_count = np.sum(predictions[:, 1] > threshold)  # Count frames predicted as fake
    total_frames = len(predictions)
    print(f"Total Frames: {total_frames}, Fake Frames: {fake_count}")
    if fake_count / total_frames > 0.5:
        print("The video is likely a deep fake.")
    else:
        print("The video is likely real.")

# Call with different thresholds
predict_deepfake(preprocessed_frames, model, threshold=0.6)
