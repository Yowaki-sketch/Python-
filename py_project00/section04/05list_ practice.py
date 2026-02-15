"""
sum()函数：容器元素求和
len()函数：返回容器长度
max()函数 求最大值
min()函数 求最小值
"""
# 1.定义列表
num_list = []
# 2.输入10个元素
for i in range(10):
    num = int(input("请输入一个正整数"))
    num_list.append(num)
print("当前数字列表为：", num_list)

# 3.排序
num_list.sort()
print("排序后的数字列表为：", num_list)

# 4.输出该容器的最大值，最小值以及平均值
print("容器里的最大值：", max(num_list))
print("容器里的最大值：", num_list[-1])
print("最小值：", num_list[0])
print("最小值：", min(num_list))
print("平均值为：", sum(num_list) / len(num_list))





