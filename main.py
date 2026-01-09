import cv2
from mss import mss
import numpy as np
import pyautogui
import cvzone



def capture_screen_region_opencv(x,y,desired_width,desired_height):
    ss = pyautogui.screenshot(region=(x,y,desired_width,desired_height))
    ss = np.array(ss)
    ss = cv2.cvtColor(ss,cv2.COLOR_RGB2BGR)
    return ss

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

while True:
    imgGame = capture_screen_region_opencv(250,250,750,250)

    cp = 100,150,110
    imgCrop = imgGame[cp[0]:cp[1],cp[2]:]
    
    imgPre = preprocess(imgCrop)

    imgContours, conFound = find_obstacles(imgCrop,imgPre)

    cv2.imshow('Game',imgGame)
    cv2.imshow('imgCrop',imgCrop)
    cv2.imshow('imgContour',imgContours)
    
    if cv2.waitKey(30)==27:
        break