"""
range:范围，界限；视觉（或听觉）范围；射程，射击距离；一系列；
range()函数，获得int数字集
range(end)
range(start,end)
range(start,end ,step)
step为步长，也就是取数字的间隔
"""

collect = range(1, 101)  # 获取1到100的整数集
collect01 = range(0, 50)  # 0到49
collect02 = range(50, 100, 2)  # 0,2,4,6

for i in collect:
    print(i, end=",")

print()

for i in collect02:
    print(i,end=",")
