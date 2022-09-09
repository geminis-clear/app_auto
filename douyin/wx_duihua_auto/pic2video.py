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
from PIL import Image
import os
import moviepy.editor as mov


def video(name):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    cap_fps = 0.5

    size = (376, 688)
    save_path = f'video/{name}.mp4'
    video = cv2.VideoWriter(save_path, fourcc, cap_fps, size)

    path = f'./imgs/{name}/'
    file_list = os.listdir(path)
    print(file_list)
    for filename in file_list:
        if 'png' in filename:
            img = cv2.imread(path + filename)
            img = cv2.resize(img, size)
            video.write(img)
    video.release()
    set_bg_music(save_path)


def set_bg_music(videofile):
    print(videofile)
    print('添加背景音乐')
    # 初始化视频文件对象
    clip = mov.VideoFileClip(videofile)
    # # 从某个视频中提取一段背景音乐
    # audio = mov.AudioFileClip('./source.mp4').subclip(0, 83)
    # # 将背景音乐写入.mp3文件
    # audio.write_audiofile('./background.mp3')
    # 向合成好的无声视频中添加背景音乐
    audio = mov.AudioFileClip('audio/1.mp3')
    clip = clip.set_audio(audio)
    # 保存视频
    clip.write_videofile(videofile)
    print('背景音乐添加完成！')


# video('rr')
set_bg_music('video/rr.mp4')