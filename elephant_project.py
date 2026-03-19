import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# 1. Load the image
# Replace 'elephant.jpg' with your photo file name
image_path = 'elephant.jpg' 
img = cv.imread(image_path)

if img is None:
    print("Error: Could not symbol or find the image.")
else:
    # 2. Detect objects in the image
    bbox, label, conf = cv.detect_common_objects(img)

    # 3. Check if an elephant is detected
    if 'elephant' in label:
        print("Success: Elephant detected in the photo!")
        
        # 4. Draw a box around the detected elephant
        output_image = draw_bbox(img, bbox, label, conf)

        # 5. Display the result
        cv.imshow("Elephant Detection", output_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("No elephant found in this image.")