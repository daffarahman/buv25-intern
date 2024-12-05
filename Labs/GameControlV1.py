# Using hand to control player

import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame

class CameraControl:
    frame = None
    ret = False
    hands = None

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.detector = HandDetector(maxHands=1, detectionCon=0.8)

    def capture(self):
        self.ret, self.frame = self.cam.read()

    def resize(self, size):
        self.frame = cv2.resize(self.frame, size)

    def detect(self):
        self.hands = self.detector.findHands(self.frame, draw=True)

    def fingers(self):
        if self.hands:
            if self.hands[0]:
                # print(self.hands[0][0]['lmList'])
                return self.detector.fingersUp(self.hands[0][0])
        
    def index_finger_direction(self):
        if self.hands:
            if self.hands[0]:
                lmlist = self.hands[0][0]['lmList']
                index_finger_tip = lmlist[8]
                x, y = index_finger_tip[:2]
                print(x, y)
                # return self.detector.fingersUp(self.hands[0][0])

    def show(self):
        cv2.imshow("CamControl", self.frame)

    def close(self):
        cv2.destroyWindow("CamControl")

    def release(self):
        self.cam.release()

    def waitKey(self, key):
        return not cv2.waitKey(1) & 0xFF == ord(key)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    
    player_pos = pygame.Vector2(50, 50)
    player_speed = 5
    
    ambatufish = pygame.transform.scale(pygame.image.load("./gfx/playerfish.png").convert_alpha(), (150, 200))
    lake = pygame.transform.scale(pygame.image.load("./gfx/lake.png").convert_alpha(), (300, 300))
    mission_passed = pygame.transform.scale(pygame.image.load("./gfx/mission-passed.png").convert_alpha(), (800, 600))

    cc = CameraControl()

    win = False
    while cc.waitKey('q'):
        
        # Camera Detector
        cc.capture()
        cc.detect()
        cc.frame = cv2.flip(cc.frame, 1)

        # user input
        finger = cc.fingers()
        if finger:
            cc.index_finger_direction()
            if finger.count(1) == 1:
                player_pos.y -= player_speed
            if finger.count(1) == 2:
                player_pos.y += player_speed
            if finger.count(1) == 3:
                player_pos.x += player_speed
            if finger.count(1) == 4:
                player_pos.x -= player_speed

        # cc.resize((400, 300))
        cc.show()
        # End Camera Detector

        # Game Logic
        window.fill("green")

        # pygame.draw.circle(window, "blue", player_pos, 30)
        
        if player_pos.x >= 415 and player_pos.x <= 605 and player_pos.y >= 250 and player_pos.y <= 410:
            win = True

        if not win:
            window.blit(lake, (400, 300))
            window.blit(ambatufish, player_pos)
        else:
            window.blit(mission_passed, (0, 0))

        pygame.display.flip()
        # End Game Logic

    cc.close()
    cc.release()

    pygame.quit()
