import cv2

input_video_path = "three.mp4"
output_video_path = "three_resized.mp4"

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get the original video's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# print(width, height)

new_width = 1920
new_height = 1080

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use different codecs based on your needs
out = cv2.VideoWriter(output_video_path, fourcc, 30, (new_width, new_height))


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Write the resized frame to the output video
    out.write(resized_frame)

# Release the video capture and writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
