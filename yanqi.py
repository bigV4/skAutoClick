'''
Mac/Linux/Windows通过命令调用浏览器打开某网页
Mac:
#open 'http://blog.csdn.net/jiezhi2013'
Linux:
#x-www-browser 'http://blog.csdn.net/jiezhi2013'
Windows:
#cmd /c start http://blog.csdn.net/jiezhi2013
由此可以很容易从我们的程序里来调用浏览器打开某网页了。
'''
import pyautogui
import datetime
import random
import time
import os
import string

time.sleep(3)

# Mac计算器的按钮截图
xiangqing = 'xiangqing.png'  # xiangqing
yanqitu = 'yanqi.png'  # yanqi
yizhou = 'yizhou.png'  # yizhou
erzhou = 'erzhou.png'  # 等于号
queren = 'queren.png'
xiazai = 'xiazai.png'
cunchu = 'cunchu.png'

# 图片识别和点击的函数

# 屏幕尺寸
width, height = pyautogui.size()
width_half = int(width / 2)
height_half = int(height / 2)
width_part = int(width / 4)
height_part = int(height / 4)
print(pyautogui.size())


def randommove():
    # 鼠标随机移动1-3秒，以表示程序已经开始运行
    for i in range(0, random.randint(1, 3)):
        # 生成坐标
        x = random.randint(1, width)
        y = random.randint(1, height)
        print("randommove", x, y)
        # 移动鼠标
        pyautogui.moveTo(x, y, duration=1)
    return x, y


def find_and_click(image):
    #x1, y1 = randommove()
    # move1(3)
    try:
        x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
        print(pyautogui.locateOnScreen(image))
        (x1, y1) = pyautogui.locateOnScreen(image)[0:2]
        print("左上角：", image, x, y)
        print("中心点：", image, x1, y1)
        pyautogui.moveTo(x/2, y/2, duration=0.75)
        time.sleep(0.25)
        pyautogui.moveTo(x/2, y/2, duration=0.75)
        pyautogui.click(x/2, y/2)
    except Exception as e:
        print("image", image, e)


def yanqi(xlh):
    os.system("open 'https://lm.dev-rs.com/license_admin/license/?search=%s'" % xlh)
    for i in range(0, 60):
        if pyautogui.locateCenterOnScreen("jiemian.png", confidence=0.9):
            break
        else:
            print("time.sleep(1)")
            time.sleep(0.25)
    pyautogui.moveTo(width/4, height/4, duration=1)
    pyautogui.click(width/4, height/4)
    find_and_click(xiangqing)
    for i in range(0, 30):
        time.sleep(0.25)
        if pyautogui.locateCenterOnScreen(yanqitu, confidence=0.9):
            break
        else:
            print("%s press down" % i)
            pyautogui.press('down')
    find_and_click(yanqitu)
    time.sleep(0.25)
    find_and_click(yizhou)
    time.sleep(0.25)
    find_and_click(erzhou)
    time.sleep(0.25)
    find_and_click(queren)
    time.sleep(0.25)
    find_and_click(queren)
    time.sleep(0.25)
    find_and_click(xiazai)
    time.sleep(0.25)
    find_and_click(cunchu)


# 执行5*8=
yanqi("1PX4BKFF1HA")
