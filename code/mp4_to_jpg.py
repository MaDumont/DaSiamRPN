import cv2
import numpy as np
import os

# set video file path of input video with name and extension
vid = cv2.VideoCapture('./video/second_video_prism_john.mp4')


output_folder_name = 'images'


if not os.path.exists(output_folder_name):
    os.makedirs(output_folder_name)

#for frame identity
index = 0
while(index < 200):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret: 
        break

    height, width, depth= frame.shape
    frame = cv2.resize(frame,(1080,745))
    # Saves images
    name = './' + output_folder_name + '/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1
