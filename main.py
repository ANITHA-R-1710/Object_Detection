import cv2
from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

print("Object Detection and Tracking Started!")
print("Press 'q' to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture video.")
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.5
    )

    # Draw bounding boxes and tracking IDs
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()