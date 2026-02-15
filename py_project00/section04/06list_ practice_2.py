"""
in 是一个运算符，结果是一个布尔值，查看容器中是否包含指定元素
not in 是否不包含指定元素
"""
# 1.定义列表
num_list1 = [17, 56, 33, 55, 46, 97, 13, 25]
num_list2 = [155, 36, 99, 45, 987, 77, 13, 25]

# 合并列表
for num in num_list2:
    if num not in num_list1:  # 如果不存在则添加
        num_list1.append(num)
print(num_list1)

num_list1.sort()
print(num_list1)

flog = 47 in num_list2  # todo:布尔表达式 语法：元素 in 列表
print(flog)

# todo:解包 -> 将容器解开成一个个独立的元素
# 语法：*列表名
num_list = [*num_list1, *num_list2]
print(num_list)
# 组包 列表直接加
num_list = num_list1 + num_list2
print(num_list)
# 还可以用extend（）方法
num_list1.extend(num_list2)  # 不会产生新的列表而是吧参数位置的列表合并到主调列表
print(num_list1)
