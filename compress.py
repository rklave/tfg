from email.mime import image

import numpy as np
import cv2
import time
import subprocess
time_start = time.clock()
#run your code

cap = cv2.VideoCapture('3D_11_LEFT.mp4')
#cap = cv2.VideoCapture(0)
# Get the frames per second of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the number of frames of the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'VP80')
cont = 0
cont2 = 0
#cont3 = 0
op = '.\Proves\output' + str(cont2) + ".avi"
#important to put same resolution as the video.
out = cv2.VideoWriter(op, fourcc, 30.0, (1920, 1080))
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        cont = cont + 1
        if cont == 10:
            out.write(frame)
            opc1 = '.\Proves\outputC' + str(cont2) + ".avi"
            subprocess.check_output("ffmpeg -y -i " + op + " -c:v libx264 -s 480x270 " + opc1)
            cont2 = cont2 + 1
            op = ".\Proves\output" + str(cont2) + ".avi"
            out = cv2.VideoWriter(op, fourcc, 30.0, (1920, 1080))
            time_elapsed = (time.clock() - time_start)
            time_start = time.clock()
            cont = 0
        else:
            out.write(frame)
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()