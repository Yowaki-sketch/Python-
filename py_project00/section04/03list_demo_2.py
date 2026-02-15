"""
切片：针对操作数据容器截取其中一部分的操作。
其实就是 访问/获取容器的一部分不能省略的只有第一个冒号：
序列类型容器特点 -> 有索引
todo:列表，字符串，元组等序列类型容器都支持切片操作。
切片语法：容器名[开始索引:结束索引:步长]
1.只加开始索引默认从开始截取到最后，如果是负数索引那就是从负数索引开始到最后，如果不写默认从头开始
TODO：依旧是包前不包后，反向索引嘛就是方向相反
2.不包含结束索引无论正负：
3.步长就是间隔，不写的话默认就是1
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_piece = my_list[0:5]
# 切片打印
print(list_piece)
list_piece01 = my_list[-5:]
print(list_piece01)

list_piece02 = my_list[:5]  # 不写默认从头开始
print(list_piece02)

# 正数负数的混合切片
list_piece03 = my_list[1:-2:2]
print(list_piece03)

# 只指定步长
list_piece04 = my_list[::2]
print(list_piece04)

# 指定步长为负数则会倒序
list_piece05 = my_list[::-1]
print(list_piece05)

list_piece06 = my_list[1:9]  # end参数超出索引和不写一个效果
print(list_piece06)
