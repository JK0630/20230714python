import numpy as np
import cv2 as cv
import random as rd
width = 1024
height= 600
depth = 3
thickness = -1 # e.g. -1, 1, 10, ......
offset_x = 50
offset_y = 20
x = 55
y = 22
screen_start_x = 100
screen_start_y = 500
bgr = (0, 255, 0)
count = 15
while True:
    img = np.zeros(shape = (height, width, depth)) # img = np.zeros((height, width, depth), np.uint8)
    
    for i in range(count): 
        bar_cnt = rd.randint(1,6)
        
        for j in range(bar_cnt):
            start_x = screen_start_x + i * x
            start_y = screen_start_y - j * y
            cv.rectangle(img, (start_x, start_y), (start_x + offset_x, start_y + offset_y), bgr, thickness)

    cv.imshow("test",img)
    cv.waitKey(100)