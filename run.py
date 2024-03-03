#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/31 15:59
@Auth ： Xq
@File ：run_demo.py
@IDE ：PyCharm
"""
import os

import cv2
import mss
import time
from pynput.mouse import Controller
from pynput.mouse import Button
import numpy as np
import pyautogui
import pygetwindow as gw

from FindSoft.Find_Exe import FindExeTools

pyautogui.pause_time = 1.5


class FindImageCoordinates(object):

    def __init__(self):
        pass

    def find_icon_coordinates(self, image_path):
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
            threshold = 0.8
            locations = np.where(result >= threshold)

            # 提取匹配位置的坐标
            icon_height, icon_width = scaled_icon.shape
            coordinates.extend(list(zip(locations[1], locations[0])))

        # 确定最准确的位置
        most_probable_coordinate = self.find_most_probable_coordinate(coordinates, screenshot, icon)

        # 在原始截图上绘制矩形框显示最准确的位置
        if most_probable_coordinate is not None:
            x, y = most_probable_coordinate
            cv2.rectangle(screenshot, (x, y), (x + icon_width, y + icon_height), (0, 255, 0), 2)

        # 保存包含标记的结果图像
        cv2.imwrite('result.png', screenshot)

        return most_probable_coordinate[0], most_probable_coordinate[1]

    def find_most_probable_coordinate(self, coordinates, screenshot, icon):
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


class RunSunLogin(object):

    def __init__(self):
        self.sun_desk = F'Images{os.sep}ScreenshotImage{os.sep}sun_desk.png'
        self.devices = F'Images{os.sep}ScreenshotImage{os.sep}devices.png'
        self.search_wfname = F'Images{os.sep}ScreenshotImage{os.sep}search_wfname.png'
        self.crlh = F'Images{os.sep}ScreenshotImage{os.sep}crlh_7460.png'
        self.ahqs = F'Images{os.sep}ScreenshotImage{os.sep}ahqs_9907.png'
        self.desk_control = F'Images{os.sep}ScreenshotImage{os.sep}desk_control.png'

    def sun_login(self):
        FIC = FindImageCoordinates()
        sun_desk_x, sun_desk_y = FIC.find_icon_coordinates(self.sun_desk)
        pyautogui.moveTo(sun_desk_x, sun_desk_y)
        pyautogui.doubleClick()
        time.sleep(5)

        # devices_x, devices_y = FIC.find_icon_coordinates(self.devices)
        # pyautogui.moveTo(devices_x, devices_y)
        # pyautogui.doubleClick()

        time.sleep(2)
        devices_x, devices_y = FIC.find_icon_coordinates(self.search_wfname)
        pyautogui.moveTo(devices_x, devices_y)
        pyautogui.doubleClick()
        time.sleep(2)

        pyautogui.press('7')
        pyautogui.press('4')
        pyautogui.press('6')
        pyautogui.press('0')
        time.sleep(2)

        crlh_x, crlh_y = FIC.find_icon_coordinates(self.crlh)
        pyautogui.moveTo(crlh_x, crlh_y)
        pyautogui.doubleClick()
        time.sleep(2)

        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.desk_control)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
    def sun_login_ahqs(self):
        FIC = FindImageCoordinates()
        sun_desk_x, sun_desk_y = FIC.find_icon_coordinates(self.sun_desk)
        pyautogui.moveTo(sun_desk_x, sun_desk_y)
        pyautogui.doubleClick()
        time.sleep(5)

        # devices_x, devices_y = FIC.find_icon_coordinates(self.devices)
        # pyautogui.moveTo(devices_x, devices_y)
        # pyautogui.doubleClick()

        time.sleep(2)
        devices_x, devices_y = FIC.find_icon_coordinates(self.search_wfname)
        pyautogui.moveTo(devices_x, devices_y)
        pyautogui.doubleClick()
        time.sleep(2)

        pyautogui.press('9')
        pyautogui.press('9')
        pyautogui.press('0')
        pyautogui.press('7')
        time.sleep(2)

        crlh_x, crlh_y = FIC.find_icon_coordinates(self.ahqs)
        pyautogui.moveTo(crlh_x, crlh_y)
        pyautogui.doubleClick()
        time.sleep(2)

        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.desk_control)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)


class RemoteConnection(object):
    def __init__(self):
        self.goole_browser = F'Images{os.sep}ScreenshotImage{os.sep}goole_browser.png'
        self.qianxin_browser = F'Images{os.sep}ScreenshotImage{os.sep}qianxin_browser.png'
        self.qianxin_browser_choose = F'Images{os.sep}ScreenshotImage{os.sep}qianxin_browser_choose.png'
        self.goole_browser_choose = F'Images{os.sep}ScreenshotImage{os.sep}goole_browser_choose.png'
        self.goole_browser1 = F'Images{os.sep}ScreenshotImage{os.sep}goole_browser1.png'
        self.wind_farm = F'Images{os.sep}ScreenshotImage{os.sep}wind_farm.png'
        self.drop_list = F'Images{os.sep}ScreenshotImage{os.sep}drop_list.png'
        self.crlh_name = F'Images{os.sep}ScreenshotImage{os.sep}crlh_name.png'
        self.ahqs_name = F'Images{os.sep}ScreenshotImage{os.sep}ahqs_name.png'
        self.login_name = F'Images{os.sep}ScreenshotImage{os.sep}login_name.png'
        self.login_password = F'Images{os.sep}ScreenshotImage{os.sep}login_password.png'
        self.login_password_ahqs = F'Images{os.sep}ScreenshotImage{os.sep}login_password_ahqs.png'
        self.login_button = F'Images{os.sep}ScreenshotImage{os.sep}login_button.png'
        self.dispatch = F'Images{os.sep}ScreenshotImage{os.sep}dispatch.png'

    def max_screen(self):
        soft_name3 = F'长润龙湖风电场7460'
        WGC = WinGenericClass()
        WGC.max_soft(soft_name3)
        time.sleep(6)
    def max_screen_ahqs(self):
        soft_name3 = F'安华强胜风电场9907'
        WGC = WinGenericClass()
        WGC.max_soft(soft_name3)
        time.sleep(6)
    def open_browser(self):
        time.sleep(5)
        FIC = FindImageCoordinates()
        try:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.goole_browser)
        except:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.goole_browser_choose)

        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
        pyautogui.doubleClick()
        time.sleep(2)
    def open_browser_ahqs(self):
        FIC = FindImageCoordinates()
        try:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.qianxin_browser)
        except:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.qianxin_browser_choose)

        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        time.sleep(2)
    def open_browser1(self):
        time.sleep(5)
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.goole_browser1)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        time.sleep(2)

    def open_dispatch(self):
        time.sleep(5)

        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.dispatch)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_wind_farm(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.wind_farm)
        pyautogui.moveTo(desk_control_x + 5, desk_control_y + 5)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_drop_list(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.drop_list)
        # 移动鼠标到下拉框上面
        mouse = Controller()
        mouse.position = (desk_control_x + 5, desk_control_y + 5)

        time.sleep(0.1)
        # 点开下拉框
        mouse.click(Button.left, 1)
        time.sleep(0.1)

        # # 移动鼠标到下拉框选项上面
        mouse.position = (desk_control_x + 10, desk_control_y - 10)

        for i in range(100):

            try:
                pyautogui.scroll(-10)
                time.sleep(1)
                FIC = FindImageCoordinates()
                desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.crlh_name)
                pyautogui.moveTo(desk_control_x + 5, desk_control_y + 5)
                pyautogui.doubleClick()
                pyautogui.doubleClick()
                time.sleep(2)
                print(f"成功找到并点击了图片，坐标为({desk_control_x}, {desk_control_x})")
                break
            except Exception as e:
                print(F'没有找到风电场{e}')
                pass

    def choose_drop_list_ahqs(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.drop_list)
        # 移动鼠标到下拉框上面
        mouse = Controller()
        mouse.position = (desk_control_x + 5, desk_control_y + 5)

        time.sleep(0.1)
        # 点开下拉框
        mouse.click(Button.left, 1)
        time.sleep(0.1)

        # # 移动鼠标到下拉框选项上面
        mouse.position = (desk_control_x + 10, desk_control_y - 10)

        for i in range(100):

            try:
                pyautogui.scroll(-10)
                time.sleep(1)
                FIC = FindImageCoordinates()
                desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.crlh_name)
                pyautogui.moveTo(desk_control_x + 5, desk_control_y + 5)
                pyautogui.doubleClick()
                pyautogui.doubleClick()
                time.sleep(2)
                print(f"成功找到并点击了图片，坐标为({desk_control_x}, {desk_control_x})")
                break
            except Exception as e:
                print(F'没有找到风电场{e}')
                pass

    def choose_login_name(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.login_name)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_login_password(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.login_password)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_login_password_ahqs(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.login_password_ahqs)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_login_button(self):
        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.login_button)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)


class WebpageDataReport(object):
    def __init__(self):
        # self.fdycgl = F'Images{os.sep}ScreenshotImage{os.sep}fdycgl.png'
        self.fdcryxxx = F'Images{os.sep}ScreenshotImage{os.sep}fdcryxxx.png'
        self.drop_list = F'Images{os.sep}ScreenshotImage{os.sep}drop_list.png'
        self.crlh_name = F'Images{os.sep}ScreenshotImage{os.sep}crlh_name.png'
        self.login_name = F'Images{os.sep}ScreenshotImage{os.sep}login_name.png'
        self.login_password = F'Images{os.sep}ScreenshotImage{os.sep}login_password.png'
        self.login_button = F'Images{os.sep}ScreenshotImage{os.sep}login_button.png'
        self.fill = F'Images{os.sep}ScreenshotImage{os.sep}fill.png'
        self.save_data = F'Images{os.sep}ScreenshotImage{os.sep}save_data.png'
        self.save_data_crlh = F'Images{os.sep}ScreenshotImage{os.sep}save_dat_crlh.png'
        self.save_data_ahqs = F'Images{os.sep}ScreenshotImage{os.sep}save_data_ahqs.png'
        self.cdmc = F'Images{os.sep}ScreenshotImage{os.sep}cdmc.png'
        self.fdycgl = F'Images{os.sep}ScreenshotImage{os.sep}fdycgl.png'
        self.fdycgl1 = F'Images{os.sep}ScreenshotImage{os.sep}fdycgl1.png'
        self.fdcryxxx = F'Images{os.sep}ScreenshotImage{os.sep}fdcryxxx.png'
        self.confirm_save = F'Images{os.sep}ScreenshotImage{os.sep}confirm_save.png'
        self.confirm_save_ahqs = F'Images{os.sep}ScreenshotImage{os.sep}confirm_save_ahqs.png'
        self.confirm_report = F'Images{os.sep}ScreenshotImage{os.sep}confirm_report.png'
        self.confirm_report_ahqs= F'Images{os.sep}ScreenshotImage{os.sep}confirm_report_ahqs.png'
        self.confirm_report_crlh= F'Images{os.sep}ScreenshotImage{os.sep}confirm_report_crlh.png'
        self.tianbao_crlh = F'Images{os.sep}ScreenshotImage{os.sep}tianbao_crlh.png'
        self.tianbao_kuang_qhqs = F'Images{os.sep}ScreenshotImage{os.sep}tianbao_kuang_ahqs.png'
        self.tianbao_kuang_crlh = F'Images{os.sep}ScreenshotImage{os.sep}tianbao_kuang_crlh.png'

        self.fill_list = self.fill_list_return()

    def fill_list_return(self):
        fill_list = [
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_rfdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_kyfdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_llfdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_rzwxdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_rznszdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_ybjrdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_rzddl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_rzdszdl.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_10mgpjfs.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_10mgzdfs.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_10mgjdfs.png',  # 11
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_pjqw.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_zgqw.png',
            # F'Images{os.sep}ScreenshotImage{os.sep}fill_zdqw.png',
            F'Images{os.sep}ScreenshotImage{os.sep}tianbao_crlh.png',

        ]
        return fill_list

    def choose_fdycgl(self):
        time.sleep(2)

        FIC = FindImageCoordinates()
        try:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.fdycgl)
        except:
            desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.fdycgl1)

        time.sleep(2)  # 82 20
        # 100 350
        #  133 636
        print(desk_control_x, desk_control_y, 2222222222222222)
        pyautogui.moveTo(desk_control_x - 30, desk_control_y)
        # pyautogui.moveTo(103, 353)
        pyautogui.doubleClick()
        time.sleep(2)

        # for _ in range(14):
        #     pyautogui.press('tab')
        #     time.sleep(2)
        # pyautogui.press('enter')  # 登录
        # time.sleep(2)
        # for _ in range(6):
        #     pyautogui.press('tab')
        #     time.sleep(2)
        # pyautogui.press('enter')  # 登录
        # time.sleep(2)
        #
        # for _ in range(26):
        #     pyautogui.press('tab')
        #     time.sleep(2)
        # for i in range(14):
        #     pyautogui.typewrite('123455', interval=2)
    def choose_fdyryxxx1(self):
        time.sleep(3)

        FIC = FindImageCoordinates()
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.fdcryxxx)
        time.sleep(3)

        pyautogui.moveTo(desk_control_x, desk_control_y)
        time.sleep(2)
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_fdyryxxx(self):
        time.sleep(3)

        button_x, button_y = pyautogui.locateCenterOnScreen(self.fdcryxxx, confidence=0.6)

        # 移动鼠标到按钮位置并点击
        pyautogui.moveTo(button_x, button_y)
        time.sleep(2)

        pyautogui.doubleClick()
        pyautogui.doubleClick()

        # 等待2秒后关闭软件
        time.sleep(2)
    def select_crlh_data(self):
        crlh_data = WinGenericClass().select_crlh()
        data1 = crlh_data[1]
        data2 = crlh_data[1]
        data3 = crlh_data[1]
        data4 = crlh_data[1]
        data5 = crlh_data[1]
        data6 = crlh_data[1]
        data7 = crlh_data[1]
        data8 = crlh_data[1]
        data9 = crlh_data[1]
        data10 = crlh_data[1]
        data11 = crlh_data[1]
        data12 = crlh_data[1]
        data13 = crlh_data[1]
        data14 = crlh_data[1]

    def choose_fill1(self):
        time.sleep(3)
        crlh_data = WinGenericClass().select_crlh()

        desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_kuang, confidence=0.8)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick(desk_control_x,desk_control_y)
        print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        wf_name = crlh_data[0]
        now_day=  crlh_data[1]
        swdl =    float(crlh_data[2])
        data1 =  swdl
        zwxdl = float(crlh_data[12])
        data2 = swdl+ zwxdl
        znssdl = crlh_data[4]
        data3 = swdl+ zwxdl+znssdl
        data4 = zwxdl
        data5 = znssdl
        data6 = crlh_data[5]
        data7 = crlh_data[3]
        data8 = crlh_data[13]
        data9 = crlh_data[6]
        data10 = crlh_data[7]
        data11 = crlh_data[8]
        data12 = crlh_data[10]
        data13 = crlh_data[9]
        data14 = crlh_data[11]
        crlh_data_list = []
        crlh_data_list.append(data1)
        crlh_data_list.append(data2)
        crlh_data_list.append(data3)
        crlh_data_list.append(data4)
        crlh_data_list.append(data5)
        crlh_data_list.append(data6)
        crlh_data_list.append(data7)
        crlh_data_list.append(data8)
        crlh_data_list.append(data9)
        crlh_data_list.append(data10)
        crlh_data_list.append(data11)
        crlh_data_list.append(data12)
        crlh_data_list.append(data13)
        crlh_data_list.append(data14)
        pyautogui.press('tab', interval=1)
        time.sleep(1)
        pyautogui.press('tab', interval=1)
        time.sleep(1)
        for i in crlh_data_list:
            pyautogui.press('tab', interval=2)
            time.sleep(2)
            pyautogui.typewrite(str(i),interval=2)
            time.sleep(1)


        # pyautogui.press('tab', interval=1)
        #
        # pyautogui.press('tab', interval=1)



        # for i in range(11):
        #     desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_crlh, confidence=0.8)
        #
        #     desk_control_x, desk_control_y = desk_control_x + 100, desk_control_y + 20
        #     pyautogui.moveTo(desk_control_x, desk_control_y)
        #     print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        #     pyautogui.click()
        #     WinGenericClass().choose_all()
        #
        #     pyautogui.typewrite(F"1", interval=1)  # 日发电量
        #     pyautogui.press('tab', interval=1)
        #     kygl = float(crlh_data[14]) + float(crlh_data[12]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{2}", interval=1)  # 可用发电量
        #     pyautogui.press('tab', interval=1)
        #     llfdl = float(crlh_data[14]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{3}", interval=1)  # 理论发电量
        #     pyautogui.press('tab', interval=1)  # 日站外受阻电量
        #     pyautogui.typewrite(F"{4}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日站内受阻电量
        #     pyautogui.typewrite(F"{5}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 样板机日发电量
        #     pyautogui.typewrite(F"{6}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大电量
        #     pyautogui.typewrite(F"{7}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大受阻电量
        #     pyautogui.typewrite(F"{8}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均风速
        #     pyautogui.typewrite(F"{9}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{10}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{11}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最高气温
        #     pyautogui.typewrite(F"{12}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温8
        #     pyautogui.typewrite(F"{13}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温
        #     pyautogui.typewrite(F"{14}", interval=1)
        #
        #     time.sleep(2)
    def choose_fill1_ahqs(self):
        time.sleep(3)
        crlh_data = WinGenericClass().select_ahqs()

        desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_kuang_qhqs, confidence=0.8)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick(desk_control_x,desk_control_y)
        print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        wf_name = crlh_data[0]
        now_day=  crlh_data[1]
        swdl =    float(crlh_data[2])
        data1 =  swdl
        zwxdl = float(crlh_data[12])
        data2 = swdl+ zwxdl
        znssdl = crlh_data[4]
        data3 = swdl+ zwxdl+znssdl
        data4 = zwxdl
        data5 = znssdl
        data6 = crlh_data[5]
        data7 = crlh_data[3]
        data8 = crlh_data[13]
        data9 = crlh_data[6]
        data10 = crlh_data[7]
        data11 = crlh_data[8]
        data12 = crlh_data[10]
        data13 = crlh_data[9]
        data14 = crlh_data[11]
        crlh_data_list = []
        crlh_data_list.append(data1)
        crlh_data_list.append(data2)
        crlh_data_list.append(data3)
        crlh_data_list.append(data4)
        crlh_data_list.append(data5)
        crlh_data_list.append(data6)
        crlh_data_list.append(data7)
        crlh_data_list.append(data8)
        crlh_data_list.append(data9)
        crlh_data_list.append(data10)
        crlh_data_list.append(data11)
        crlh_data_list.append(data12)
        crlh_data_list.append(data13)
        crlh_data_list.append(data14)
        pyautogui.press('tab', interval=1)
        time.sleep(1)
        pyautogui.press('tab', interval=1)
        time.sleep(1)
        for i in crlh_data_list:
            pyautogui.press('tab', interval=2)
            time.sleep(2)
            pyautogui.typewrite(str(i),interval=2)
            time.sleep(1)


        # pyautogui.press('tab', interval=1)
        #
        # pyautogui.press('tab', interval=1)



        # for i in range(11):
        #     desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_crlh, confidence=0.8)
        #
        #     desk_control_x, desk_control_y = desk_control_x + 100, desk_control_y + 20
        #     pyautogui.moveTo(desk_control_x, desk_control_y)
        #     print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        #     pyautogui.click()
        #     WinGenericClass().choose_all()
        #
        #     pyautogui.typewrite(F"1", interval=1)  # 日发电量
        #     pyautogui.press('tab', interval=1)
        #     kygl = float(crlh_data[14]) + float(crlh_data[12]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{2}", interval=1)  # 可用发电量
        #     pyautogui.press('tab', interval=1)
        #     llfdl = float(crlh_data[14]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{3}", interval=1)  # 理论发电量
        #     pyautogui.press('tab', interval=1)  # 日站外受阻电量
        #     pyautogui.typewrite(F"{4}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日站内受阻电量
        #     pyautogui.typewrite(F"{5}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 样板机日发电量
        #     pyautogui.typewrite(F"{6}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大电量
        #     pyautogui.typewrite(F"{7}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大受阻电量
        #     pyautogui.typewrite(F"{8}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均风速
        #     pyautogui.typewrite(F"{9}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{10}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{11}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最高气温
        #     pyautogui.typewrite(F"{12}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温8
        #     pyautogui.typewrite(F"{13}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温
        #     pyautogui.typewrite(F"{14}", interval=1)
        #
        #     time.sleep(2)
    def choose_fill1_crlh(self):
        time.sleep(3)
        crlh_data = WinGenericClass().select_crlh()

        desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_kuang_crlh, confidence=0.8)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick(desk_control_x,desk_control_y)
        print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        wf_name = crlh_data[0]
        now_day=  crlh_data[1]
        swdl =    float(crlh_data[2])
        data1 =  swdl
        zwxdl = float(crlh_data[12])
        data2 = swdl+ zwxdl
        znssdl = crlh_data[4]
        data3 = swdl+ zwxdl+znssdl
        data4 = zwxdl
        data5 = znssdl
        data6 = crlh_data[5]
        data7 = crlh_data[3]
        data8 = crlh_data[13]
        data9 = crlh_data[6]
        data10 = crlh_data[7]
        data11 = crlh_data[8]
        data12 = crlh_data[10]
        data13 = crlh_data[9]
        data14 = crlh_data[11]
        crlh_data_list = []
        crlh_data_list.append(data1)
        crlh_data_list.append(data2)
        crlh_data_list.append(data3)
        crlh_data_list.append(data4)
        crlh_data_list.append(data5)
        crlh_data_list.append(data6)
        crlh_data_list.append(data7)
        crlh_data_list.append(data8)
        crlh_data_list.append(data9)
        crlh_data_list.append(data10)
        crlh_data_list.append(data11)
        crlh_data_list.append(data12)
        crlh_data_list.append(data13)
        crlh_data_list.append(data14)
        # pyautogui.press('tab', interval=1)
        # time.sleep(1)
        # pyautogui.press('tab', interval=1)
        # time.sleep(1)
        for i in crlh_data_list:
            pyautogui.press('tab', interval=1)
            time.sleep(2)
            pyautogui.typewrite(str(i),interval=1)
            time.sleep(1)


        # pyautogui.press('tab', interval=1)
        #
        # pyautogui.press('tab', interval=1)



        # for i in range(11):
        #     desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(self.tianbao_crlh, confidence=0.8)
        #
        #     desk_control_x, desk_control_y = desk_control_x + 100, desk_control_y + 20
        #     pyautogui.moveTo(desk_control_x, desk_control_y)
        #     print(desk_control_x, desk_control_y, 10000, self.tianbao_crlh)
        #     pyautogui.click()
        #     WinGenericClass().choose_all()
        #
        #     pyautogui.typewrite(F"1", interval=1)  # 日发电量
        #     pyautogui.press('tab', interval=1)
        #     kygl = float(crlh_data[14]) + float(crlh_data[12]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{2}", interval=1)  # 可用发电量
        #     pyautogui.press('tab', interval=1)
        #     llfdl = float(crlh_data[14]) + float(crlh_data[12])
        #     pyautogui.typewrite(F"{3}", interval=1)  # 理论发电量
        #     pyautogui.press('tab', interval=1)  # 日站外受阻电量
        #     pyautogui.typewrite(F"{4}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日站内受阻电量
        #     pyautogui.typewrite(F"{5}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 样板机日发电量
        #     pyautogui.typewrite(F"{6}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大电量
        #     pyautogui.typewrite(F"{7}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 日最大受阻电量
        #     pyautogui.typewrite(F"{8}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均风速
        #     pyautogui.typewrite(F"{9}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{10}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最大风速
        #     pyautogui.typewrite(F"{11}", interval=1)
        #
        #     pyautogui.press('tab', interval=1)  # 最高气温
        #     pyautogui.typewrite(F"{12}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温8
        #     pyautogui.typewrite(F"{13}", interval=1)
        #     pyautogui.press('tab', interval=1)  # 平均气温
        #     pyautogui.typewrite(F"{14}", interval=1)
        #
        #     time.sleep(2)

    def choose_fill_llfdl(self):
        crlh_data = WinGenericClass().select_crlh()

        time.sleep(3)

        for i in self.fill_list:
            if self.fill_list.index(i) == 10:
                time.sleep(0.2)

                desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(i, confidence=0.8)
                # 2001 564
                # 1868 540
                # 111 2006 540
                # 111 2010 564
                desk_control_x = desk_control_x + 120
                desk_control_y = desk_control_y + 20
                pyautogui.moveTo(desk_control_x, desk_control_y)
                print(66666, desk_control_x, desk_control_y)
                time.sleep(0.1)

                pyautogui.click()
                WinGenericClass().choose_all()
                time.sleep(0.2)
                for _ in range(4):
                    pyautogui.press('backspace')
                time.sleep(0.1)
                pyautogui.typewrite(F"{crlh_data[8]}", interval=1)
                time.sleep(0.2)
            if self.fill_list.index(i) == 13:
                time.sleep(0.5)

                desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(i, confidence=0.8)
                # 2001 564
                # 1868 540
                # 111 2006 540
                # 111 2010 564
                pyautogui.moveTo(desk_control_x + 120, desk_control_y + 20)
                time.sleep(0.1)

                pyautogui.click()
                WinGenericClass().choose_all()
                time.sleep(0.2)
                for _ in range(4):
                    pyautogui.press('backspace')
                time.sleep(0.1)

                pyautogui.typewrite(F"{crlh_data[11]}", interval=1)
                time.sleep(0.2)

            else:
                print(i)
                desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(i, confidence=0.8)
                # 136/26
                # 636/587
                # 627/561
                print(33333, desk_control_x, desk_control_y)

                pyautogui.moveTo(desk_control_x + 10, desk_control_y + 20)
                pyautogui.click()
                WinGenericClass().choose_all()
                time.sleep(0.2)
                for _ in range(4):
                    pyautogui.press('backspace')
                if self.fill_list.index(i) == 0:  # 日发电量
                    pyautogui.typewrite(F"{crlh_data[2]}", interval=1)
                if self.fill_list.index(i) == 1:  # 可用功率
                    pyautogui.typewrite(F"{crlh_data[14]}", interval=1)
                if self.fill_list.index(i) == 2:  # 理论发电量
                    pyautogui.typewrite(F"{crlh_data[15]}", interval=1)
                if self.fill_list.index(i) == 3:  # 日站外受阻电量
                    pyautogui.typewrite(F"{crlh_data[12]}", interval=1)
                if self.fill_list.index(i) == 4:  # 日站内受阻电量
                    pyautogui.typewrite(F"{crlh_data[12]}", interval=1)
                if self.fill_list.index(i) == 5:  # 样板机日发电量110.41
                    pyautogui.typewrite(F"{crlh_data[5]}", interval=1)
                if self.fill_list.index(i) == 6:  # 日最大电量
                    pyautogui.typewrite(F"{round(float(crlh_data[3]))}", interval=1)
                if self.fill_list.index(i) == 7:  # 日最大受阻电量
                    pyautogui.typewrite(F"{crlh_data[13]}", interval=1)
                if self.fill_list.index(i) == 8:  # 平均风速
                    pyautogui.typewrite(F"{crlh_data[6]}", interval=1)
                if self.fill_list.index(i) == 9:  # 最大风速
                    pyautogui.typewrite(F"{crlh_data[7]}", interval=1)

                if self.fill_list.index(i) == 11:  # 最高气温
                    pyautogui.typewrite(F"{crlh_data[10]}", interval=1)
                if self.fill_list.index(i) == 12:  # 平均气温
                    pyautogui.typewrite(F"{crlh_data[9]}", interval=1)

                time.sleep(0.2)
        for i in self.fill_list:
            if self.fill_list.index(i) == 9:
                desk_control_x, desk_control_y = pyautogui.locateCenterOnScreen(i, confidence=0.8)
                # 136/26
                # 636/587
                # 627/561
                print(33333, desk_control_x, desk_control_y)

                pyautogui.moveTo(desk_control_x + 10, desk_control_y + 20)
                pyautogui.click()
                WinGenericClass().choose_all()
                time.sleep(0.2)
                for _ in range(4):
                    pyautogui.press('backspace')
                pyautogui.typewrite(F"{crlh_data[7]}", interval=1)

    def choose_fill_kyfdl(self):
        FIC = FindImageCoordinates()
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.fill_kyfdl)

        pyautogui.moveTo(desk_control_x + 45, desk_control_y + 25)
        pyautogui.click()

        time.sleep(1)
        for _ in range(4):
            pyautogui.press('backspace')

        pyautogui.typewrite(F'{9999}', interval=1)
        time.sleep(2)

    def choose_save_data(self):
        FIC = FindImageCoordinates()
        print(999999999)
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.save_data_crlh)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
    def choose_save_data_ahqs(self):
        FIC = FindImageCoordinates()
        print(999999999)
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.save_data_ahqs)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)

    def choose_confirm_save_crlh(self):
        FIC = FindImageCoordinates()
        print("开始点击安华强上报@")
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.confirm_save)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
        print("已经点击安华强")

    def choose_confirm_save_ahqs(self):
        FIC = FindImageCoordinates()
        print("开始点击安华强上报@")
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.confirm_save_ahqs)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
        print("已经点击安华强")


    def choose_confirm_report_ahqs(self):
        FIC = FindImageCoordinates()
        print("choose_confirm_report")
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.confirm_report_ahqs)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)
    def choose_confirm_report_crlh(self):
        FIC = FindImageCoordinates()
        print("choose_confirm_report")
        time.sleep(3)
        desk_control_x, desk_control_y = FIC.find_icon_coordinates(self.confirm_report_crlh)
        pyautogui.moveTo(desk_control_x, desk_control_y)
        pyautogui.doubleClick()
        time.sleep(2)


class WinGenericClass(object):
    def __init__(self):
        pass

    def return_desk(self):
        time.sleep(2)

        # 模拟按下Ctrl键
        pyautogui.keyDown('win')
        # 模拟按下D键
        pyautogui.press('d')
        pyautogui.keyUp('win')
        time.sleep(5)

    def choose_all(self):
        # 模拟按下Ctrl键
        pyautogui.keyDown('ctrl')

        # 模拟按下A键
        pyautogui.press('a')

        # 松开Ctrl键
        pyautogui.keyUp('ctrl')

    def moveto_doubleclick(self, button_x, button_y):
        pyautogui.moveTo(button_x, button_y)
        time.sleep(0.1)
        pyautogui.doubleClick()

    def max_soft(self, soft_name):
        res = gw.getWindowsWithTitle(F'{soft_name}')[0]
        res.maximize()

    def select_crlh(self):
        from DataBaseInfo.MysqlInfo.MysqlTools import MysqlCurd

        new_nanfang = R'DataBaseInfo/MysqlInfo/new_nanfang.yml'
        MC = MysqlCurd(new_nanfang)
        from datetime import date, timedelta
        today = date.today()
        yesterday = today - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')

        query_sql = F"SELECT * FROM `data_oms数据源_吉林` WHERE 风电场='长润龙湖' and 日期='{formatted_yesterday}'"
        res = MC.query_sql(query_sql)
        return res[0]

    def select_ahqs(self):
        from DataBaseInfo.MysqlInfo.MysqlTools import MysqlCurd

        new_nanfang = R'DataBaseInfo/MysqlInfo/new_nanfang.yml'
        MC = MysqlCurd(new_nanfang)
        from datetime import date, timedelta
        today = date.today()
        yesterday = today - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')

        query_sql = F"SELECT * FROM `data_oms数据源_吉林` WHERE 风电场='安华强胜' and 日期='{formatted_yesterday}'"
        res = MC.query_sql(query_sql)
        return res[0]


class SavePushDing():
    def __init__(self):
        # 天润
        self.jf_token = F'c8eb8d7b8fe2a3c07843233bf225082126db09ab59506bd5631abef4304da29e'
        # 奈卢斯
        self.nls_token = F'acabcf918755694f2365051202cf3921a690594c1278e4b7fe960186dce58977'
        # 天润
        self.appkey = "dingtc3bwfk9fnqr4g7s"  # image测试
        self.appsecret = "C33oOe03_K5pitN_S2dUppBwgit2VnPW0yWnWYBM3GzogGKhdy2yFUGREl9fLICU"  # image测试
        self.chatid = "chatf3b32d9471c57b4a5a0979efdb06d087"  # image测试
        # 奈卢斯
        self.nls_appkey = "dingjk2duanbfvbywqzx"  # image测试
        self.nls_appsecret = "ICYb4-cvsvIk5DwuZY9zehc5UbpldqIClzS6uuIYFrhjU9z11guV6lold1qNqc2k"  # image测试
        self.nls_chatid = "chatf8ef1e955cf2c4e83a7e776e0011366c"  # image测试
        self.message_crlh = {
            "msgtype": "markdown",
            "markdown": {
                "title": "长润龙湖数据推送",
                "text":
                    F'长润龙湖数据推送'
            }
        }
        self.message_ahqs = {
            "msgtype": "markdown",
            "markdown": {
                "title": "安华强胜数据推送",
                "text":
                    F'安华强胜数据推送'
            }
        }

    def pic_save_crlh(self):
        from PIL import ImageGrab

        # 截取整个屏幕并保存为图片文件
        screen = ImageGrab.grab()
        screen.save("crlh.png")
        from DingInfo.DingBotMix import DingApiTools
        # 天润
        DAT = DingApiTools(appkey_value=self.appkey, appsecret_value=self.appsecret, chatid_value=self.chatid)
        DAT.push_message(self.jf_token, self.message_crlh)
        DAT.send_file("crlh.png", 0)

        # 奈卢斯
        DATNLS = DingApiTools(appkey_value=self.nls_appkey, appsecret_value=self.nls_appsecret,
                              chatid_value=self.nls_chatid)
        DATNLS.push_message(self.nls_token, self.message_crlh)
        DATNLS.send_file("crlh.png", 0)
    def pic_save_ahqs(self):
        from PIL import ImageGrab

        # 截取整个屏幕并保存为图片文件
        screen = ImageGrab.grab()
        screen.save("ahqs.png")
        from DingInfo.DingBotMix import DingApiTools
        # 天润
        DAT = DingApiTools(appkey_value=self.appkey, appsecret_value=self.appsecret, chatid_value=self.chatid)
        DAT.push_message(self.jf_token, self.message_ahqs)
        DAT.send_file("ahqs.png", 0)

        # 奈卢斯
        DATNLS = DingApiTools(appkey_value=self.nls_appkey, appsecret_value=self.nls_appsecret,
                              chatid_value=self.nls_chatid)
        DATNLS.push_message(self.nls_token, self.message_ahqs)
        DATNLS.send_file("ahqs.png", 0)


def run_crlh():
    WGC = WinGenericClass()
    RCS = RemoteConnection()
    WDR = WebpageDataReport()
    RSL = RunSunLogin()
    # #
    #
    # WGC.return_desk()
    # FT = FindExeTools()
    # soft_name = F'SunloginRemote.exe'
    # FT.find_soft_kill(soft_name)
    # RSL.sun_login()
    # RCS.max_screen()
    # # WGC.return_desk()
    # for _ in range(5):
    #     time.sleep(0.1)
    #
    #     # 模拟按下Ctrl键
    #     pyautogui.keyDown('win')
    #     # 模拟按下D键
    #     pyautogui.press('d')
    #     pyautogui.keyUp('win')
    #     time.sleep(0.1)
    #     pyautogui.keyDown('alt')
    #     pyautogui.press('f4')
    #     pyautogui.keyUp('alt')
    #     # 添加一个小延迟以确保每次按键操作都能被系统识别
    #     time.sleep(0.1)
    # time.sleep(2)
    # for _ in range(2):
    #     RCS.open_browser()
    #
    # time.sleep(2)
    # pyautogui.press('f11')
    # time.sleep(1)
    # pyautogui.press('f11')
    # time.sleep(1)
    #
    # pyautogui.press('f11')
    # time.sleep(1)
    # try:
    #     RCS.open_dispatch()
    # except Exception as e:
    #     print(1, e)
    # # pyautogui.press('tab')
    # # time.sleep(2)
    # # for _ in range(3):
    # #     pyautogui.press('right')
    # #     time.sleep(2)
    # # pyautogui.press('tab')
    # # time.sleep(2)
    # # pyautogui.press('enter')
    # # time.sleep(2)
    # #
    # # # for _ in range(66):
    # # for _ in range(65):
    # #     pyautogui.press('down', interval=0.5)
    # #
    # # pyautogui.press('enter')
    # # time.sleep(1)
    # # pyautogui.press('tab')
    # # time.sleep(2)
    # # pyautogui.typewrite('crlhfdc', interval=2)
    # # # pyautogui.typewrite('ahqsfdc', interval=2)
    # # time.sleep(2)
    # # pyautogui.press('tab')
    # # time.sleep(2)
    # # pyautogui.typewrite('crlhfdc283', interval=2)
    # # # pyautogui.typewrite('ahqsfdc298', interval=2)
    # # pyautogui.press('tab')
    # # time.sleep(2)
    # # pyautogui.press('enter')  # 登录
    # # time.sleep(2)
    # RCS.choose_wind_farm()
    # RCS.choose_drop_list()
    # RCS.choose_login_name()
    # RCS.choose_login_password()
    # RCS.choose_login_button()
    # # #

    # try:
    #     WDR.choose_fdycgl()
    # except Exception as e:
    #     print("choose_fdycgl", e)
    #     WDR.choose_fdycgl()
    # WDR.choose_fdyryxxx()
    # WDR.choose_fill_llfdl()
    # WDR.choose_fill1()
    # WDR.choose_fill1_crlh()
    try:
        WDR.choose_save_data()
    except Exception as e:
        WDR.choose_save_data()

    try:
        WDR.choose_confirm_save_crlh()
    except Exception as e:
        WDR.choose_confirm_save_crlh()
    try:
        WDR.choose_confirm_save_crlh()
    except Exception as e:
        WDR.choose_confirm_save_crlh()

    try:
        WDR.choose_confirm_report_crlh()
    except Exception as e:
        WDR.choose_confirm_report_crlh()
    try:
        WDR.choose_confirm_save_crlh()
    except Exception as e:
        WDR.choose_confirm_save_crlh()

    SPD = SavePushDing()
    SPD.pic_save_crlh()

def run_ahqs():
    WGC = WinGenericClass()
    RCS = RemoteConnection()
    WDR = WebpageDataReport()
    RSL = RunSunLogin()
    # #
    #
    # WGC.return_desk()
    # FT = FindExeTools()
    # soft_name = F'SunloginRemote.exe'
    # FT.find_soft_kill(soft_name)
    # RSL.sun_login_ahqs()
    # RCS.max_screen_ahqs()
    # WGC.return_desk()
    # for _ in range(5):
    #     time.sleep(0.1)
    #
    #     # 模拟按下Ctrl键
    #     pyautogui.keyDown('win')
    #     # 模拟按下D键
    #     pyautogui.press('d')
    #     pyautogui.keyUp('win')
    #     time.sleep(0.1)
    #     pyautogui.keyDown('alt')
    #     pyautogui.press('f4')
    #     pyautogui.keyUp('alt')
    #     # 添加一个小延迟以确保每次按键操作都能被系统识别
    #     time.sleep(0.1)
    #     RCS.open_browser_ahqs()
    # pyautogui.press('f11')
    # time.sleep(1)
    # pyautogui.press('f11')
    # time.sleep(1)
    #
    # pyautogui.press('f11')
    # time.sleep(4)
    # print("界面最大话")
    # # try:
    # #     RCS.open_dispatch()
    # # except Exception as e:
    # #     print(871, e)
    # time.sleep(3)
    # pyautogui.press('tab', interval=0.1)
    # time.sleep(2)
    # for _ in range(4):
    #     pyautogui.press('right')
    #     time.sleep(2)
    # pyautogui.press('tab')
    # print("选择")
    #
    # time.sleep(2)
    # pyautogui.press('enter')
    # time.sleep(2)

    # for _ in range(66):
    # for _ in range(75):
    #     pyautogui.press('down', interval=0.5)
    #
    # pyautogui.press('enter')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(2)
    #
    # # pyautogui.typewrite('crlhfdc283', interval=2)
    # for i in 'ahqsfdc298':
    #     pyautogui.press(i,interval=0.5)
      # pyautogui.press('h',interval=0.5)
      # pyautogui.press('q',interval=0.5)
      # pyautogui.press('s',interval=0.5)
      # pyautogui.press('f',interval=0.5)
      # pyautogui.press('d',interval=0.5)
      # pyautogui.press('c',interval=0.5)


    # pyautogui.typewrite('ahqsfdc', interval=2)
    # pyautogui.press('tab')
    # time.sleep(2)
    # pyautogui.press('enter')  # 登录
    # time.sleep(2)
    # for i in 'ahqsfdc298':
    #       pyautogui.press(i,interval=0.5)
    #
    #
    #
    # # pyautogui.typewrite('ahqsfdc298', interval=2)
    # pyautogui.press('tab')
    # time.sleep(2)
    # pyautogui.press('enter')  # 登录
    # time.sleep(2)
    # RCS.choose_wind_farm()
    # RCS.choose_drop_list()
    # RCS.choose_login_name()
    # RCS.choose_login_password()
    # RCS.choose_login_button()
    # #

    # try:
    #     WDR.choose_fdycgl()
    # except Exception as e:
    #     print("choose_fdycgl", e)
    #     WDR.choose_fdycgl()
    # # WDR.choose_fdyryxxx()
    # WDR.choose_fill_llfdl()
    WDR.choose_fill1_ahqs()
    try:
        WDR.choose_save_data_ahqs()
    except Exception as e:
        WDR.choose_save_data_ahqs()

    try:
        WDR.choose_confirm_save_ahqs()
    except Exception as e:
        WDR.choose_confirm_save_ahqs()
    try:
        WDR.choose_confirm_save_ahqs()
    except Exception as e:
        WDR.choose_confirm_save_ahqs()


    try:
        WDR.choose_confirm_report_ahqs()
    except Exception as e:
        WDR.choose_confirm_report_ahqs()
    SPD = SavePushDing()
    SPD.pic_save_ahqs()

if __name__ == '__main__':
    run_crlh()
    # run_ahqs()
5.4
