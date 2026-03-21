import cv2
import mediapipe as mp
import time
import winsound

# 1. Setup Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

# Variables to track time
sleep_start_time = 0
is_sleeping = False

print("System Active... Press 'q' to Exit")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Using specific points for the eyelids
            # Point 159 (Top) and 145 (Bottom)
            top = face_landmarks.landmark[159].y
            bottom = face_landmarks.landmark[145].y
            
            eye_distance = bottom - top

            # Check if eyes are closed (Threshold)
            if eye_distance < 0.012:
                if not is_sleeping:
                    sleep_start_time = time.time()
                    is_sleeping = True
                
                # Calculate how long eyes have been closed
                time_closed = time.time() - sleep_start_time

                if time_closed > 1.5:  # If closed for more than 1.5 seconds
                    cv2.putText(frame, "ALARM! WAKE UP!", (50, 150), 
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
                    winsound.Beep(2500, 500) # Loud Beep
            else:
                is_sleeping = False
                cv2.putText(frame, "STATUS: AWAKE", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Smart Drowsiness Alert', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()