"""
Python的循环特色：
todo：while后面可以接else

"""

# while True:  # 标准无限循环
#     print("无线循环")


a = 1
b = 2

while a <= 10:
    print(f"目前a的值为{a}")
    a += 1  # 迭代因子
else:  # todo:接else的效果,不太理解有啥意义
    print(f"a的值目前为{a}已大于10")
    print("循环正常结束")
