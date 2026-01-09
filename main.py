import cv2
from mss import mss
import numpy as np
import pyautogui


def capture_screen_region_opencv(x,y,desired_width,desired_height):
    ss = pyautogui.screenshot(region=(x,y,desired_width,desired_height))
    ss = np.array(ss)
    ss = cv2.cvtColor(ss,cv2.COLOR_RGB2BGR)
    return ss
