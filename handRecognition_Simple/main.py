



import cv2, mediapipe as mp

cap = cv2.VideoCapture("hand.mp4")
fps, prev_frame, prev_center = cap.get(cv2.CAP_PROP_FPS),\
    None, None
hands = mp.solutions.hands.Hands(static_image_mode=False,
max_num_hands=2, min_detection_confidence=0.5)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.resize(frame, (600, 900))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in \
                results.multi_hand_landmarks:
            mp.\
            solutions.drawing_utils.draw_landmarks(frame,
            hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            center_x, center_y = \
            int(hand_landmarks.
            landmark[mp.solutions.hands.HandLandmark.WRIST].x *
            frame.shape[1]), \
            int(hand_landmarks.
            landmark[mp.solutions.hands.HandLandmark.WRIST].y *
            frame.shape[0])
            prev_center = (center_x, center_y)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()











