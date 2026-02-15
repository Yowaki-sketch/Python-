"""
todo:列表推导式：快速简洁构建新列表的语法
语法格式：要插入容器的值 for i in 数据源容器 是否插入的条件判断
"""
num_list1 = []
for i in range(1, 21):
    num_list1.append(i ** 2)
print(num_list1)

# 要插入的值可以是一个表达式
num_list2 = [(i ** 2) for i in range(1, 21)]
print(num_list2)

# 列表推导式,后面还可以加条件判断
num_list3 = [i for i in num_list2 if i % 2 == 0]
print(num_list3)
