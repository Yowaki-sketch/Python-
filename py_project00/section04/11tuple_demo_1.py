"""
todo:元组(tuple)与列表相似，但是最大特点->不可变
元组一旦被定义就不可修改(只读)
可以冲村不同类型的值，有索引
支持切片
"""
# 基本操作

tup01 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7)  # 元组定义
print(tup01)
print(type(tup01))

print(tup01[0])

# tup01[1] = 7  # 不可修改

# 切片，但是切片可以。todo相当于一次性访问或者获取容器中的多个元素

tup_piece = tup01[0:5]
print(tup_piece)
print(type(tup_piece))  # 切片后得到的容器仍然是元组

# count()方法，统计元素数量
count = tup01.count(7)
print(count)
# index()方法 ，查找指定元素的索引，若不存在则会报错
# tu_index = tup01.index(11)
tu_index = tup01.index(7)
print(tu_index)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7]
# li_index = my_list.index(15)  # 在list中，用index()查找不存在的元素也会报错
li_index = my_list.index(5)

print(li_index)

# 元组的注意点定义单元素元组，唯一元素后面要加逗号
tup02 = ()  # 这是一个空元组
tup03 = (3)  # 这么写只是一个不同的变量
tup04 = (4,)  # todo:往唯一元素的后面加一个逗号，它就是个单元素元组了
t2_type = type(tup02)
t3_type = type(tup03)
t4_type = type(tup04)
print("这是一个空元素的元组", t2_type)
print("这只是一个普通int变量", t3_type)
print("加一个逗号它才会是一个单元素元组", t4_type)
