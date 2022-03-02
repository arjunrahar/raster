#!/usr/bin/env python3
import os
import pickle as pkl
import numpy as np
from plyfile import PlyData
import ctypes as ct
import cv2
import random
from random import randint
from random import shuffle
from tqdm import tqdm
from scipy import stats
from glob import glob
from argparse import ArgumentParser


h, w = 480, 640
bg_img_pth_lst = glob("SUN2012pascalformat/JPEGImages/*.jpg")
bg = None
len_bg_lst = len(bg_img_pth_lst)
while bg is None or len(bg.shape) < 3:
    print(1)
    bg_pth = bg_img_pth_lst[randint(0, len_bg_lst-1)]
    bg = cv2.imread(bg_pth)
    wind = 'bg'
  
# Using cv2.imshow() method 
# Displaying the image  
    # cv2.imshow(wind, bg)
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows()
   
    if len(bg.shape) < 3:
        bg = None
        continue
    bg_h, bg_w, _ = bg.shape
    print(bg_h,bg_w)
    if bg_h < h:
        new_w = int(float(h) / bg_h * bg_w)
        bg = cv2.resize(bg, (new_w, h))
    bg_h, bg_w, _ = bg.shape
    if bg_w < w:
        new_h = int(float(w) / bg_w * bg_h)
        bg = cv2.resize(bg, (w, new_h))
    bg_h, bg_w, _ = bg.shape
    if bg_h > h:
        sh = randint(0, bg_h-h)
        bg = bg[sh:sh+h, :, :]
    bg_h, bg_w, _ = bg.shape
    if bg_w > w:
        sw = randint(0, bg_w-w)
        bg = bg[:, sw:sw+w, :]

R = np.array([[1,2,3],[4,5,6],[7,8,9]])
T =  np.array([1,2,3])
xyz = np.random.randint(10, size=(4, 3))
#print("RT", R.T)
new_xyz = np.dot(xyz, R.T) + T
print(new_xyz)