"""
列表对象/类的常用方法
append() 尾部增添
insert() 指定索引插入
extend() 尾部并和一个新容器
pop() 指定索引位置元素删除,会把删除掉的元素作为返回值返回
remove() 移除指定元素（找到的第一个）
sort() 排序/需要保证数据类型一致
reverse() 反转 和-1步长切片一个功能
"""

# 定义容器
my_list = [1, 2, 3, 4, 5, 6]

# 增
my_list.append("7")  # 尾部增添元素
my_list.insert(0, "8")  # 指定索引插入元素，后面的元素会被挤到下一个索引处
my_list.extend(["9", "10", "11"])  # 将一个新容器并和到尾部
print(my_list)
# 删
my_list.remove("10")  # 删除指定元素
ele_removed = my_list.pop(0)  # 删除指定索引位置上的元素
ele_removed2 = my_list.pop()  # 不指定索引的话删最后一个
print(my_list)
print(ele_removed)
print(ele_removed2)
# 改

my_list.reverse()  # 反转
print(my_list)

# 查

# 排序需要列表中的数据类型一致
my_list2 = [1, 2, 3, 4, 5, 5, 11, 6]
my_list2.sort()  # 不一致会报错
print(my_list2)
