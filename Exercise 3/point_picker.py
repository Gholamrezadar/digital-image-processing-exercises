import cv2
import numpy as np
import argparse


# Parse command line arguments
parser = argparse.ArgumentParser(description='Point picker')
parser.add_argument('-i', '--image', help='Path to image', required=True)
args = parser.parse_args()

# Load image
img = cv2.imread(args.image)

print(img.shape)
points_list = []
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        points_list.append([x,y])

# Create a black image, a window and bind the function to window
cv2.namedWindow('Click on left_eye, right_eye, bottom of the nose and press Esc')
cv2.setMouseCallback('Click on left_eye, right_eye, bottom of the nose and press Esc',draw_circle)

# Application Main Loop
while(1):
    cv2.imshow('Click on left_eye, right_eye, bottom of the nose and press Esc',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

with open('points.txt', 'a') as f:
    try:
        f.write(f"File name: {args.image}" + '\n\n')
        f.write(f"points[1,0,:] = {points_list[0]} # l_eye a" + "\n")
        f.write(f"points[1,1,:] = {points_list[1]} # r_eye a" + "\n")
        f.write(f"points[1,2,:] = {points_list[2]} # nose_a" + "\n\n")

        f.write(f"points[0,0,:] = {points_list[0]} # l_eye b" + "\n")
        f.write(f"points[0,1,:] = {points_list[1]} # r_eye b" + "\n")
        f.write(f"points[0,2,:] = {points_list[2]} # nose_b" + "\n")

        f.write("-"*40 + "\n")
    except:
        f.write(f"name:{args.image}:" + '\n')
        f.write(f"{points_list}\n")
        f.write("-"*40 + "\n")

import os
os.system("start points.txt")

