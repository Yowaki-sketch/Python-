"""
字典 常见操作
增删改查
todo:增加和修改是一样的语法：字典名[K] = V
"""
dict1 = {"王林": 670, "李慕婉": 608, "许立国": 580, "韩立": 688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"])  # 根据key获取value
print(dict1.get("涛哥"))  # 根据key获取value

print(dict1.keys())  # 获取所有的key
print(dict1.values())  # 获取所有的value
print(dict1.items())  # 获取所有的键值对 key:value todo:吧每个键值对封装成一个len为2的元组

# 删除
score = dict1.pop("许立国")  # 有返回值为value
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k, v in dict1.items():  # 元组解包语法
    print(f"{k} : {v}")
