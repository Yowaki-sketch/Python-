"""
最后一个猜字游戏
random模块的用法
"""

import random

rd_num = random.randint(1, 100)  # 随机数变量

while True:
    i = int(input("请输入你猜的数字"))
    if rd_num == i:
        print("你猜对了")
        break
    elif i > rd_num:
        print("大了")
    elif i < rd_num:
        print("小了")

print("该随机数是%d" % rd_num)
