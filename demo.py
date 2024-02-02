#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/18 0018 14:20
@Auth ： Xq
@File ：demo.py
@IDE ：PyCharm
"""

import cv2
import mss
import time
from pynput.mouse import Controller
from pynput.mouse import Button
import numpy as np


def find_icon_coordinates(image_path):
    # 加载要识别的图片
    icon = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 创建 MSS (Media Source) 对象
    with mss.mss() as sct:
        # 获取屏幕分辨率
        monitor = sct.monitors[1]  # 通常使用 monitor 1，根据你的设置而定

        # 截取整个屏幕
        screenshot = sct.shot(output="screenshot.png")

    # 加载要搜索的图像
    screenshot = cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)

    # 使用多尺度匹配
    scales = [0.8, 1.0, 1.2]
    coordinates = []

    for scale in scales:
        scaled_icon = cv2.resize(icon, None, fx=scale, fy=scale)

        # 使用不同的匹配方法，如 cv2.TM_CCOEFF_NORMED 或 cv2.TM_CCORR
        result = cv2.matchTemplate(screenshot, scaled_icon, cv2.TM_CCOEFF_NORMED)

        # 设置阈值，找到匹配的位置
        threshold = 0.80
        locations = np.where(result >= threshold)

        # 提取匹配位置的坐标
        icon_height, icon_width = scaled_icon.shape
        coordinates.extend(list(zip(locations[1], locations[0])))

    # 确定最准确的位置
    most_probable_coordinate = find_most_probable_coordinate(coordinates, screenshot, icon)

    # 在原始截图上绘制矩形框显示最准确的位置
    if most_probable_coordinate is not None:
        x, y = most_probable_coordinate
        cv2.rectangle(screenshot, (x, y), (x + icon_width, y + icon_height), (0, 255, 0), 2)

    # 保存包含标记的结果图像
    cv2.imwrite('result.png', screenshot)

    return most_probable_coordinate


def find_most_probable_coordinate(coordinates, screenshot, icon):
    max_score = 0
    most_probable_coordinate = None

    for (x, y) in coordinates:
        # 获取匹配结果的矩形区域
        icon_height, icon_width = icon.shape
        roi = screenshot[y:y + icon_height, x:x + icon_width]

        # 计算匹配得分
        result = cv2.matchTemplate(roi, icon, cv2.TM_CCOEFF_NORMED)
        _, score, _, _ = cv2.minMaxLoc(result)

        # 更新最大得分和对应的坐标
        if score > max_score:
            max_score = score
            most_probable_coordinate = (x, y)

    return most_probable_coordinate


# 创建鼠标控制器
mouse = Controller()

time.sleep(1)

# 选中风电厂单选坐标
fd_redio = 'fd.png'

# 调用函数并获取匹配坐标
matching_coordinates = find_icon_coordinates(fd_redio)
print(matching_coordinates)
fd_x = matching_coordinates[0]
fd_y = matching_coordinates[1]

time.sleep(1)
# 移动鼠标到风电厂单选坐标上面
mouse.position = (fd_x + 5, fd_y + 5)

time.sleep(1)
# 选中风电厂
mouse.click(Button.left, 1)
time.sleep(2)

# 选中下拉框
droplist = 'droplist.png'

# 调用函数并获取匹配坐标
matching_coordinates = find_icon_coordinates(droplist)
print(matching_coordinates)
dl_x = matching_coordinates[0]
dl_y = matching_coordinates[1]

time.sleep(1)
# 移动鼠标到下拉框上面
mouse.position = (dl_x + 5, dl_y + 5)

time.sleep(1)
# 点开下拉框
mouse.click(Button.left, 1)
time.sleep(2)

# # 移动鼠标到下拉框选项上面
mouse.position = (dl_x + 10, dl_y - 10)

# 滑动滚轮选择目标
time.sleep(2)

for i in range(100):
    mouse.scroll(0, -30)
    time.sleep(1)
    # 选中长润龙湖风电厂
    longhu = 'longhu.png'

    # 调用函数并获取匹配坐标
    matching_coordinates = find_icon_coordinates(longhu)
    if matching_coordinates:
        print(F'{matching_coordinates}')
        lh_x = matching_coordinates[0]
        lh_y = matching_coordinates[1]

        # 移动鼠标到长润龙湖风电厂选项
        mouse.position = (lh_x, lh_y )
        time.sleep(1)
        # 点开下拉框
        mouse.click(Button.left, 1)
        time.sleep(2)
        break
    else:
        print(F'no match{i}')


