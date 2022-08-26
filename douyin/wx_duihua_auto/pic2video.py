# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/22 14:48
@Author  : maiYang
@Site    : 
@File    : pic2video.py
@desc    : 图片转视频
"""
import cv2
import os

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
cap_fps = 30

size = (376, 688)
video = cv2.VideoWriter('result.mp4', fourcc, cap_fps, size)

path = './'
file_list = os.listdir(path)
print(file_list)
for filename in file_list:
    if 'png' in filename:
        img = cv2.imread(path + filename)
        img = cv2.resized(img, size)
        video.write(img)
video.release()
