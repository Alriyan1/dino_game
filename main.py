import cv2
from mss import mss
import numpy as np
import pyautogui
import cvzone
from cvzone.FPS import FPS

fpsReader = FPS()



def capture_screen_region_opencv(x,y,desired_width,desired_height):
    ss = pyautogui.screenshot(region=(x,y,desired_width,desired_height))
    ss = np.array(ss)
    ss = cv2.cvtColor(ss,cv2.COLOR_RGB2BGR)
    return ss

def capture_screen_region_opencv_mss(x,y,widht,height):
    with mss() as sct:
        monitor = {'top':y,'left':x,'width':widht,'height':height}
        ss = sct.grab(monitor)
        img = np.array(ss)
        img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)

        return img


def preprocess(imgCrop):
    gray_frame = cv2.cvtColor(imgCrop,cv2.COLOR_BGR2GRAY)
    _,binary_frame = cv2.threshold(gray_frame,127,255,cv2.THRESH_BINARY_INV)
    canny_frame = cv2.Canny(binary_frame,50,50)
    kernel = np.ones((5,5))
    dilated_frame = cv2.dilate(canny_frame,kernel,iterations=1)
    return dilated_frame

def find_obstacles(imgCrop,imgPre):
    imgContours,conFound = cvzone.findContours(imgCrop,imgPre,minArea=100,filter=None)
    return imgContours,conFound

def game_logic(conFound,imgContours,jump_distance=90):
    if conFound:
        left_most_contour = sorted(conFound,key=lambda x:x['bbox'][0])

        cv2.line(imgContours,(0,left_most_contour[0]['bbox'][1]+10),
                 (left_most_contour[0]['bbox'][0],left_most_contour[0]['bbox'][1]+10),(0,200,0),10)
        
        if left_most_contour[0]['bbox'][0]<jump_distance:
            pyautogui.press('space')

    return imgContours

while True:
    imgGame = capture_screen_region_opencv_mss(250,250,750,250)

    cp = 100,160,110
    imgCrop = imgGame[cp[0]:cp[1],cp[2]:]
    
    imgPre = preprocess(imgCrop)

    imgContours, conFound = find_obstacles(imgCrop,imgPre)

    imgContours = game_logic(conFound,imgContours)

    imgGame[cp[0]:cp[1],cp[2]:]=imgContours
    
    fps, imgGame = fpsReader.update(imgGame)

    cv2.imshow('Game',imgGame)
    # cv2.imshow('imgCrop',imgCrop)
    # cv2.imshow('imgContour',imgContours)
    
    if cv2.waitKey(30)==27:
        break