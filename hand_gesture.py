import cv2
import numpy as np
import os
import mediapipe as mp
import tensorflow as tf 
from tensorflow.python.keras.models import load_model

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Initialize the webcam for Hand Gesture Recognition Python project
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    x , y, c = frame.shape
    frame = cv2.flip(frame, 1)

    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()

framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

result = hands.process(framergb)

className = ''

  # post process the result
if result.multi_hand_landmarks:
    landmarks = []
    for handslms in result.multi_hand_landmarks:
        for lm in handslms.landmark:
              # print(id, lm)
            lmx = int(lm.x * x)
            lmy = int(lm.y * y)

            landmarks.append([lmx, lmy])

          # Drawing landmarks on frames
        mpDraw.draw_landmarks(frame, handslms, 
mpHands.HAND_CONNECTIONS)
