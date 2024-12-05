# Opening Video

import cv2

cap = cv2.VideoCapture("cat.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # show frame
    cv2.imshow('Videoo', frame)

    # input mask
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
