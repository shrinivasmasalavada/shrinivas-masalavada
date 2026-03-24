from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")  # lightweight model (good for embedded)

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not working")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("AI Object Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()