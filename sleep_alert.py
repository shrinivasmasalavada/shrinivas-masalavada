import cv2
import dlib
from scipy.spatial import distance
import winsound # Use 'import os' for Mac/Linux

# Function to calculate Eye Aspect Ratio (EAR)
def calculate_ear(eye):
    # Vertical distances
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    # Horizontal distance
    C = distance.euclidean(eye[0], eye[3])
    # EAR Formula
    ear = (A + B) / (2.0 * C)
    return ear

# Load Dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Eye landmark indices for Dlib
L_EYE = [42, 43, 44, 45, 46, 47]
R_EYE = [36, 37, 38, 39, 40, 41]

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        
        # Extract eye coordinates
        left_eye = []
        right_eye = []
        for n in L_EYE:
            left_eye.append((landmarks.part(n).x, landmarks.part(n).y))
        for n in R_EYE:
            right_eye.append((landmarks.part(n).x, landmarks.part(n).y))

        # Calculate EAR for both eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        # Threshold: If EAR is less than 0.25, eyes are closed
        if avg_ear < 0.25:
            cv2.putText(frame, "SLEEPING! UTTO BETA!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            winsound.Beep(2500, 500) # Loud high-pitched beep
        else:
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Advanced Drowsiness Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()