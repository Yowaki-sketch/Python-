"""
set集合
可自动去重，无索引,可以修改
add()添加元素
remove()移除指定的元素，todo:若集合中不存在这个元素则会报错
pop() 随即删除元素并返回， 啊？
clear() 清空集合
todo：下面方法结果均为返回值
 difference() 求两个集合的差 主调集合中包含的元素
 union() 合并集合：求2个集合的并集
 intersection() 求2个集合的交集
"""

# 定义
# 构造器定义
s = set()  # 空集合（set）,在控制台的表示也是set()，这是为了和字典进行区分
s2 = {"5", "5", "ui", "oo", 4, 5, 66, 4}  # todo:添加的重复元素会被自动去除,且顺序是根据哈希值?确定
print(s)
print(s2)
print("s的类型是：", type(s))
print("s2的类型是：", type(s2))
# 特点：用s3 = {}这种方式定义出的是字典(dict)而非集合
s3 = {}
print("s的类型是：", type(s3))

# 常用方法

s.add(True)
s.add(None)
s.add("ching")
s.add(12)
s.add(5)
s.add(6)
print("添加元素后的集合")
print(s)
s.clear()
print("清空后的集合:", s)

# 交际和并集

s_alphabet1 = {"A", "B", "C", "D", "E", "F", "G", "H", "I"}
s_alphabet2 = {"H", "I", "J", "K", "L", "M", "N"}

intersection = s_alphabet1.intersection(s_alphabet2)
union = s_alphabet1.union(s_alphabet2)
difference = s_alphabet1.difference(s_alphabet2)

print("2个集合的交集为：", intersection)
print("2个集合的并集为：", union)
print("2个集合的差集为：", difference, "该差集只包括主调集合里的差集部分")
