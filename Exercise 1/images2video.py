import cv2
import numpy as np
import imageio

# choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('pacman_final_seed42_5.avi', fourcc, 8, (192, 248))

imglst = []
for i in range(0, 210):
    img = cv2.imread("pacman_results/maze_"+str(i) + '.png')
    imglst.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    video.write(img)

cv2.destroyAllWindows()
video.release()

imageio.mimsave('video5.gif', imglst, fps=8)
