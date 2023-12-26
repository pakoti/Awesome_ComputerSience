#this program will track a black object that were given to him

import cv2

# Load the image you want to track
image_to_track = cv2.imread(r'C:\Users\johnsnow\Documents\GitHub\Awesome_ComputerSience\Programming_Languages_Lab\ImageProcessing\image.png')  # Replace 'image_to_track.png' with your image file
gray_image_to_track = cv2.cvtColor(image_to_track, cv2.COLOR_BGR2GRAY)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 or -1 for default webcam, or replace with the specific webcam index

# Get the width and height of the image
image_height, image_width, _ = image_to_track.shape[:3]

while True:
    ret, frame = cap.read()  # Capture frame-by-frame from the webcam
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Try to find the image within the frame
    result = cv2.matchTemplate(gray_frame, gray_image_to_track, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc  # Top-left corner of the matched area
    bottom_right = (top_left[0] + image_width, top_left[1] + image_height)  # Bottom-right corner of the matched area

    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)  # Draw a green rectangle around the matched area

    # Display the frame with the rectangle drawn around the matched area
    cv2.imshow('Image Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()