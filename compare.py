# -*- coding: utf-8 -*-
"""
@Time :2022/12/15 22:06
@Author :Lai Xiangyuan
@Email :2936885192@qq.com
@File :compare.py
@ID :12003990122
"""

import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import pandas as pd


def hash_img(img):  # 计算图片的特征序列
    a = []  # 存储图片的像素
    hash_img = ''  # 特征序列
    width, height = 10, 10  # 图片缩放大小
    img = img.resize((width, height))  # 图片缩放为width×height
    for y in range(img.height):
        b = []
        for x in range(img.width):
            pos = x, y
            color_array = img.getpixel(pos)  # 获得像素
            color = sum(color_array) / 3  # 灰度化
            b.append(int(color))
        a.append(b)
    for y in range(img.height):
        avg = sum(a[y]) / len(a[y])  # 计算每一行的像素平均值
        for x in range(img.width):
            if a[y][x] >= avg:  # 生成特征序列,如果此点像素大于平均值则为1,反之为0
                hash_img += '1'
            else:
                hash_img += '0'

    return hash_img


def similar(img1, img2):  # 求相似度
    hash1 = hash_img(img1)  # 计算img1的特征序列
    hash2 = hash_img(img2)  # 计算img2的特征序列
    differnce = 0
    for i in range(len(hash1)):
        differnce += abs(int(hash1[i]) - int(hash2[i]))
    similar = 1 - (differnce / len(hash1))
    return similar


@st.cache
def find(capture_img):
    s = []
    for i in range(0, 1000):
        img2 = Image.open('picture/' + str(i) + '.png')
        s.append([i, similar(capture_img, img2)])
    for i in range(0, len(s) - 1):
        for j in range(0, len(s) - 1 - i):
            if s[j][1] < s[j + 1][1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s


def get():
    st.header("简易图像搜索引擎")
    st.sidebar.header("请在边栏上传图片：")
    uploaded_file = st.sidebar.file_uploader("在这传", type='png')
    choice = st.sidebar.selectbox("这里是相似度最高的三张照片，请选择：",
                                  ["png1", "png2", "png3"])
    col1, col2 = st.columns(2)
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # 将字节数据转化成字节流
        bytes_data = BytesIO(bytes_data)
        # Image.open()可以读字节流
        capture_img = Image.open(bytes_data)
        # capture_img = cv2.cvtColor(np.asarray(capture_img), cv2.COLOR_RGB2BGR)
        with col1:
            st.image(capture_img, width=300, caption="你上传的照片")
        s = find(capture_img)
        row = []
        column = []
        # print(s)
        for i in range(1, 20):
            row.append(s[i][0])
            column.append(s[i][1])

        if choice == 'png1':
            with col2:
                img = Image.open('picture/' + str(s[1][0]) + ".png")
                st.image(img, width=300, caption="TOP1")
        elif choice == 'png2':
            with col2:
                img = Image.open('picture/' + str(s[2][0]) + ".png")
                st.image(img, width=300, caption="TOP2")
        elif choice == 'png3':
            with col2:
                img = Image.open('picture/' + str(s[3][0]) + ".png")
                st.image(img, width=300, caption="TOP3")
        df = pd.DataFrame({
            'second column': column
        })
        st.bar_chart(df)


get()
