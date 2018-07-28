import subprocess as sp
from email.mime import image

import numpy as np
import cv2


cap = cv2.VideoCapture('.\Proves\output0.avi')
command = ['ffmpeg', '-i', ".\Proves\output0.avi", '-c:v', 'libx264', '-s', '480x270', '.\Proves\outputC0.avi']
# Get the frames per second of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the number of frames of the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(fps,num_frames)
# Define the codec and create VideoWriter object
while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()


