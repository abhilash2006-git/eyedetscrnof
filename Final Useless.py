import cv2
import numpy as np
import tkinter as tk


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')


cap = cv2.VideoCapture(0)


root = tk.Tk()
root.configure(bg='black')
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.withdraw() 

def show_black_screen():
    root.deiconify()

def hide_black_screen():
    root.withdraw()

EYEBROW_LIFT_THRESHOLD = 10  

while True:
    ret, frame = cap.read()
    if not ret:
        break

  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    eyes_detected = False
    eyebrows_lifted = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

       
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(15, 15)
        )

        if len(eyes) > 0:
            eyes_detected = True
            for (ex, ey, ew, eh) in eyes:
               
                aspect_ratio = ew / float(eh)
                if 0.8 < aspect_ratio < 2.5:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                   
                    eyebrow_region_y = max(ey - int(eh * 0.8), 0)
                    if ey - eyebrow_region_y > EYEBROW_LIFT_THRESHOLD:
                        eyebrows_lifted = True


    if eyes_detected:
        show_black_screen()
        print("Eyes detected — screen black")
    else:
        hide_black_screen()
        print("No eyes detected — screen visible")

  
    root.update()

   
    cv2.imshow('Eye & Eyebrow Detection', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
root.destroy()
