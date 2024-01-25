#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/18 0018 13:25
@Auth ： Xq
@File ：run.py
@IDE ：PyCharm
"""

import pyautogui
import pygetwindow as gw

import time

from FindSoft.Find_Exe import FindExeTools


def return_desk():
    # 模拟按下Ctrl键
    pyautogui.keyDown('win')
    # 模拟按下D键
    pyautogui.press('d')
    pyautogui.keyUp('win')


def find_desk_soft(image):
    # 获取按钮在屏幕上的位置
    button_x, button_y = pyautogui.locateCenterOnScreen(image, confidence=0.8)

    # 移动鼠标到按钮位置并点击
    pyautogui.moveTo(button_x, button_y)
    pyautogui.doubleClick()
    pyautogui.doubleClick()

    # 等待2秒后关闭软件
    time.sleep(2)


def find_soft_button(image):
    # 获取按钮在屏幕上的位置
    button_x, button_y = pyautogui.locateCenterOnScreen(image, confidence=0.8)

    # 移动鼠标到按钮位置并点击
    pyautogui.moveTo(button_x, button_y)
    pyautogui.doubleClick()
    pyautogui.doubleClick()

    # 等待2秒后关闭软件
    time.sleep(2)


def find_soft_button_one(image):
    # 获取按钮在屏幕上的位置
    button_x, button_y = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    time.sleep(1)
    # 移动鼠标到按钮位置并点击
    pyautogui.moveTo(button_x, button_y)
    pyautogui.click()

    # 等待2秒后关闭软件
    time.sleep(2)

def find_soft_button_one_tc(image):
    # 获取按钮在屏幕上的位置
    button_x, button_y = pyautogui.locateCenterOnScreen(image, confidence=0.5)
    time.sleep(1)
    # 移动鼠标到按钮位置并点击
    pyautogui.moveTo(button_x, button_y)
    pyautogui.click()

    # 等待2秒后关闭软件
    time.sleep(2)

def max_soft(soft_name):
    res = gw.getWindowsWithTitle(F'{soft_name}')[0]

    res.maximize()


def wind_(image):
    # 初始化计数器
    match_count = 0

    while match_count < 4:
        # 寻找模板在屏幕上的位置并返回其中心坐标
        position = pyautogui.locateCenterOnScreen(image)

        # 如果找到了模板（position 不为空），则增加计数器
        if position:
            match_count += 1
        else:
            # 没有找到，则可能需要稍作延时再继续查找
            time.sleep(0.1)  # 可调整延时时间以适应实际情况

        # 当找到第四个匹配项时退出循环
        if match_count == 4:
            break

    # 输出第四个匹配项的中心坐标
    if match_count == 4:
        print(f"第四个模板的中心坐标是：{position}")
        button_x = position.x
        button_y = position.y
        pyautogui.moveTo(button_x, button_y)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
    else:
        print("未能在屏幕上找到四个匹配项。")


def gundong(template_image):
    while True:
        # 寻找图片在屏幕上的位置
        location = pyautogui.locateCenterOnScreen(template_image)

        # 如果找到了图片
        if location:
            # 获取中心坐标并点击
            x, y = location
            pyautogui.click(x, y)
            print(f"成功找到并点击了图片，坐标为({x}, {y})")
            break
        else:
            # 图片未找到，可以等待一段时间再继续查找
            time.sleep(0.5)  # 可根据需要调整延时时间

    # 如果在一定时间内没有找到图片，则可能需要添加一个超时处理机制
    timeout = 60  # 设置超时时间（秒）
    start_time = time.time()

    while (time.time() - start_time) < timeout:
        print(111)
    else:
        print("在指定时间内未能找到并点击目标图片。")


def tianxie(image):
    # 获取按钮在屏幕上的位置
    BTM = list(pyautogui.locateAllOnScreen(image, confidence=0.8))
    print(BTM)
    num = 1
    print(list(BTM))
    for i in BTM:
        pyautogui.moveTo(i[0], i[1])
        # 清除输入框内容
        pyautogui.click(i)
        pyautogui.press('backspace')
        # todo 这里不能输入数值
        pyautogui.press('1')
        print(F'点击了第{num}个')
        num+=1

    # 等待2秒后关闭软件
    time.sleep(2)


if __name__ == '__main__':
    return_desk()
    FT = FindExeTools()
    soft_name = F'SunloginRemote.exe'
    FT.find_soft(soft_name)
    return_desk()
    image_name = F'2.png'
    find_desk_soft(image=image_name)
    soft_name2 = f'贝锐向日葵企业控制端'
    # max_soft(soft_name2)
    time.sleep(3)
    find_soft_button(F'3.png')
    find_soft_button_one(F'4.png')
    find_soft_button_one(F'5.png')
    find_soft_button_one(F'6.png')
    find_soft_button_one(F'7.png')

    soft_name3 = F'长润龙湖风电场7460'
    max_soft(soft_name3)
    time.sleep(6)
    try:
        find_soft_button_one_tc(F'退出.png')
    except Exception as e:
        print(F'没有推迟按钮----{e}')
        pass
    try:
        find_soft_button(F'10.png')
    except Exception as e:
        print(F'浏览器已打开--{e}')
        pass
    time.sleep(6)
    find_soft_button(F'11.png')
    time.sleep(6)
    wind_(F'12.png')
    time.sleep(6)

    find_soft_button_one(F'13.png')
    time.sleep(6)

    import pyautogui

    # # 获取当前鼠标位置
    current_mouse_x, current_mouse_y = pyautogui.position()
    print(current_mouse_x, current_mouse_y)
    pyautogui.moveTo(current_mouse_x, current_mouse_y - 100)
    print(current_mouse_x, current_mouse_y)
    time.sleep(3)
    for i in range(100):

        try:
            pyautogui.scroll(-10)
            time.sleep(3)
            location = pyautogui.locateCenterOnScreen(F'14.png')
            print(F'{location}')
            if location:
                # 获取中心坐标并点击
                x, y = location
                pyautogui.moveTo(x, y)

                pyautogui.doubleClick()
                print(f"成功找到并点击了图片，坐标为({x}, {y})")
                break
        except Exception as e:
            print(F'没有找到风电场')
            pass
    find_soft_button_one(F'17.png')
    time.sleep(3)
    find_soft_button_one(F'18.png')
    time.sleep(3)
    find_soft_button_one(F'19.png')
    time.sleep(3)
    wind_(F'20.png')
    time.sleep(3)
    find_soft_button_one(F'21.png')
    time.sleep(3)
    tianxie(F'22.png')
