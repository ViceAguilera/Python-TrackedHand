import cv2
from cvzone.HandTrackingModule import HandDetector


def main():
    width, height = 1280, 720
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = HandDetector(detectionCon=0.8)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hands, img = detector.findHands(frame)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            dataFingers = fingers
            print(dataFingers)

        img = cv2.resize(img,(0,0),None,0.5,0.5)
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()