# importing opencv
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    
    # Read the frame
    _, img = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display
    cv2.imshow('img', img)
    
    # Stop if escape key is pressed
    #cv2.imshow('img', img)
    k = cv2.waitKey(1)
    
    # wait for ESC key to exit
    if k == 27:   
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):                   # wait for 's' key to save and exit
        cv2.imwrite('messigray.png',img)
        cv2.destroyAllWindows()
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()