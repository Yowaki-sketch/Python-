"""
Python中的数据类型：
int   整数
float 小数/浮点数
str   字符串
bool  布尔
NoneType 空值
TODO:
    type()函数的使用 ->得到参数的类型 --->返回值不是字符串，而是 类型对象（type object）
    isinstance()函数的使用 ->检查传入参数是否为指定类型 --->返回布尔值
"""

# 字面量的类型
print(type("Hello"))  # 字符串类型
print(type(11))  # 整数
print(type(3.14))  # 小数
print(type(True))  # 布尔
print(type(None))  # 控制类型

miti =type("Hello")
print(miti)

# 变量的类型查看
moji = "这是个字符串"
print(type(moji))

result = isinstance(moji, str)
result2 = isinstance(moji, float)
print(result)
print(result2)
