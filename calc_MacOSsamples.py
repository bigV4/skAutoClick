import pyautogui
import datetime
import random
import time
import string

time.sleep(3)

# Mac计算器的按钮截图
five = '5.png'  # 5
eight = '8.png'  # 8
multiply = 'multiply.png'  # 乘号
equals = 'equals.png'  # 等于号

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


def move1(a):
    for i in range(0, a):
        pyautogui.moveTo(100, 300, duration=0.25)
        pyautogui.moveTo(300, 300, duration=0.25)
        pyautogui.moveTo(300, 100, duration=0.25)
        pyautogui.moveTo(150, 150, duration=0.25)


def find_and_click(image):
    #x1, y1 = randommove()
    # move1(3)
    try:
        x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
        print(pyautogui.locateOnScreen(image))
        (x1, y1) = pyautogui.locateOnScreen(image)[0:2]
        print(image, x, y)
        print(image, x1, y1)
        pyautogui.moveTo(x/2, y/2, duration=0.25)
        #pyautogui.moveTo(x, y, duration=0.25)
        time.sleep(0.25)
        pyautogui.moveTo(x1/2+1, y1/2+1, duration=0.25)
        #pyautogui.moveTo(x, y, duration=0.25)
        pyautogui.click(x1/2+1, y1/2+1)
    except Exception as e:
        print("image", image, e)


# 执行5*8=
find_and_click(five)
find_and_click(multiply)
find_and_click(eight)
find_and_click(equals)
