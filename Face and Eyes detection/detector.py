import cv2
import os
import numpy as np

file_name = None
extension = None;
for file in os.listdir('C:\\Users\\MEDA\\Desktop\\Face and Eyes detection\\uploads'):
    if file.endswith(".jpg") or file.endswith(".png"):
        file_name,extension = os.path.splitext(file)
    else:
        print("Unsupported files format")

path = r'C:\Users\MEDA\Desktop\Face and Eyes detection\uploads\%s%s'%(file_name,extension)

image = cv2.imread(path,1)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("C:\\Users\\MEDA\\Desktop\\Face and Eyes detection\\haarcascade\\haarcascade_frontalface_default.xml")

eyes_cascade = cv2.CascadeClassifier("C:\\Users\\MEDA\\Desktop\\Face and Eyes detection\\haarcascade\\haarcascade_eye.xml")

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:

    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eyes_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,128,0),2)

save_path = r'C:\Users\MEDA\Desktop\Face and Eyes detection\results\%s%s'%(file_name,extension)
cv2.imwrite(save_path,image)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
