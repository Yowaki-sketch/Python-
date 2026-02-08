"""
TODO:Python是动态类型语言，在程序运行时才进行变量类型检查，变量类型可以在程序运行中改变
"""
# 变量演示
num = 10
num = num + 3.14
print(num)

num = "bitch"
print(num)

num = True
print(num)

# 变量赋值方式
# 1.逐个赋值
base = 20
incr = 50
count = base + incr
print(count)
# 2.一次赋值多个变量,可以是不同类型变量/字面量
# todo:一条语句可以定义多个变量，也可以连续赋值
name, age = "lei", 33
print(name, age)
# 年两 = 50
# print(年两)

# 变量交换
a = 11
b = 22
tamp = a
a = b
b = tamp
print("a目前的值为:", a, "b目前的值为：", b)
