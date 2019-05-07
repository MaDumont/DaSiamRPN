# --------------------------------------------------------
# DaSiamRPN
# Licensed under The MIT License
# Written by Qiang Wang (wangqiang2015 at ia.ac.cn)
# --------------------------------------------------------
#!/usr/bin/python

import glob, cv2
import matplotlib.pyplot as plt
import numpy as np
from os.path import realpath, dirname, join

name_image_folder='easy_follow_prism'


init_rbox = [293,114 , 336,110 , 336,171 , 295,175]

im = cv2.imread('./images/frame0.jpg')  # HxWxC

cv2.rectangle(im, (init_rbox[0], init_rbox[1]), (init_rbox[4],init_rbox[5]), (0, 255, 255), 3)

cv2.imshow("fsdfs",im)

cv2.waitKey(0);

