"""
list 列表
写法：[]
相当于java中的集合ArrayList
todo：list属于 《序列类型容器》 特点 -> 有索引
最基础的数据容器
Python特性：todo:数据容器反向索引最后一个元素索引-1，前面-2一次类推
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(type(my_list))

my_list2 = [1, True, "bitch", 3.14, None, 3.14, False, 8, 9]  # 列表没有泛型，元素可以重复，有索引/下标
# 查：倒叙访问/获取元素
print(my_list2[-3])
# 改：修改元素通过赋值运算符修改
my_list2[3] = "banana"
print(my_list2)
# todo:删->通过del关键字
del my_list2[5]
print(my_list2)

# 遍历
print("遍历然后打印my_list2里的所有元素")
for item in my_list2:
    print(item)

# 异常初体验（索引越界异常）
# print(my_list2[12])
