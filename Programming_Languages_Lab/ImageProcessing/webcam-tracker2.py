import cv2

# Global variables for mouse events and rectangle selection
drawing = False
ix, iy = -1, -1

rect_complete = False
selection = (0, 0, 0, 0)

# Mouse callback function for drawing rectangle
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rect_complete, selection

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        rect_complete = False
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rect_complete = True
        selection = (min(ix, x), min(iy, y), abs(ix - x), abs(iy - y))

# Object tracking algorithm
def track_object(frame, selection):
    x, y, w, h = selection
    roi = frame[y:y+h, x:x+w]
    # Example: You can implement your object tracking algorithm here
    # For example, you can use mean shift, camshift, or any custom algorithm for tracking the object within the selected rectangle
    # Here, we'll simply draw a rectangle around the selected region as an example
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Open webcam
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_rectangle)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if not rect_complete and drawing:
        cv2.rectangle(frame, (ix, iy), (ix + 1, iy + 1), (0, 255, 0), 2)

    if rect_complete:
        track_object(frame, selection)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
