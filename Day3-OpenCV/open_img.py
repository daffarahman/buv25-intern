# Opening Image

import cv2

img = cv2.imread("HappyFish.jpg", 1)

img_width = int(img.shape[1] * 1.5)
img_height = int(img.shape[0] * 1.5)

resize = cv2.resize(img, (img_width, img_height))

while True:
    cv2.imshow("Vroooommmmm", resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
