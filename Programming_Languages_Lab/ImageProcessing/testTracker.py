import cv2
from cvlib.object_detection import draw_bbox

# Define the function to track the object
def track_object(event, x, y, flags, params):
    global selection, tracking
    if event == cv2.EVENT_LBUTTONDOWN:
        selection = (x, y, 0, 0)
        tracking = True
    elif event == cv2.EVENT_LBUTTONUP:
        selection = (selection[0], selection[1], x - selection[0], y - selection[1])
        tracking = False

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create a window to draw the rectangle
cv2.namedWindow("Tracking")
cv2.setMouseCallback("Tracking", track_object)

# Initialize the variables
selection = None
tracking = False

# Define the tracker
tracker = cv2.TrackerKCF_create()

while True:
    # Capture the frame
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        break

    # Draw the rectangle
    if selection:
        cv2.rectangle(frame, (selection[0], selection[1]), (selection[0] + selection[2], selection[1] + selection[3]), (0, 255, 0), 2)

    # Start tracking
    if tracking and selection[2] > 0 and selection[3] > 0:
        tracker.init(frame, selection)
        selection = None

    # Update the tracker
    if tracker:
        success, bbox = tracker.update(frame)
        if success:
            # Draw the bounding box
            draw_bbox(frame, [int(bbox[0]), int(bbox[1]), int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])], [0], ["Object"])

    # Display the frame
    cv2.imshow("Tracking", frame)

    # Exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy the window
cap.release()
cv2.destroyAllWindows()