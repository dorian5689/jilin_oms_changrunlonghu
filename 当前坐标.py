#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/2/2 21:26
@Auth ： Xq
@File ：当前坐标.py
@IDE ：PyCharm
"""
import os

import pyautogui
import time

try:
    while True:
        # 获取鼠标当前位置的坐标
        x, y = pyautogui.position()

        # 格式化输出坐标信息
        posStr = f"当前鼠标位置: {x}, {y}"
        print(posStr)

        # 每秒更新一次坐标
        time.sleep(1)

        # 清除控制台屏幕（Windows系统下）
        os.system('cls')
except KeyboardInterrupt:
    print("\n已退出")
#

from datetime import date
current_date = date.today()
formatted_date = current_date.strftime('%Y-%m-%d')
