import cv2
import time
import numpy as np
import os 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12, GPIO.HIGH)
recognizer= cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath= "haarcascade_frontalface_default.xml"
faceCascade= cv2.CascadeClassifier(cascadePath);
font= cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id= 0
# names related to ids: example==> Marcelo: id=1,  etc
names= ['Carina', 'Miguel', 'Antonio', 'Brayan', 'A', 'Z'] 
# Initialize and start realtime video capture
cam= cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min winAdow size to be recognized as a face
minW= 0.001*cam.get(2)
minH= 0.001*cam.get(3)
while True:
 ret, img=cam.read()
 img= cv2.flip(img, 1) # Flip vertically
 gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces= faceCascade.detectMultiScale(gray, scaleFactor= 1.2, minNeighbors= 5, minSize= (int(minW), int(minH)), )
 for(x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
  id, confidence= recognizer.predict(gray[y:y+h,x:x+w])
  # Check if confidence is less them 100==> "0" is perfect match 	
  if (confidence <50 ):
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(12,GPIO.OUT)
   id= names[id]
   GPIO.output(12, GPIO.LOW)
   #confidence= "  {0}%".format(round(120 - confidence))
   time.sleep(5)
   GPIO.cleanup()
   
  else:
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(12,GPIO.OUT)
   GPIO.output(12, GPIO.HIGH)
   id= "unknown"
   confidence= "  {0}%".format(round(100 - confidence))
  

  cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
  cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
  cv2.imshow('camera',img) 
  k= cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
  if k== 27:
   break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
GPIO.cleanup()
cv2.destroyAllWindows()
