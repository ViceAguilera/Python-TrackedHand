import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

#parametro
width, height = 1280, 720
#Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
#Dectector de manos
detector2 = HandDetector(detectionCon=0.8)
#comunicacion
com = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ('127.0.0.1', 5052)

while True:
    success, img = cap.read()
    hands, img = detector2.findHands(img)
    dataBody=[]
    dataHands=[]
    if hands:
        hand = hands[0]
        lmListHands = hand["lmList"]
        for lm in lmListHands:
            dataHands.extend([lm[0], height-lm[1], lm[2]])
        print(dataHands)

    com.sendto(str.encode(str(dataHands)), serverAddress)

    img = cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow("Video", img)
    cv2.waitKey(1)