"""
字典 :键值对容器 key：value
源：dictionary
Java中的映射（Map）
1.key不能重复(如果重复, 后面的值, 会覆盖前面的值)、
2.todo:key必须得是不可变类型（str，int，float，tuple）
    首选字符串，对象肯定不行
3.可以修改

"""
# 定义字典
# 和集合一样都是大括号
dict0 = dict()
dict00 = {}  # 等价于构造器语法
dict1 = {"王林": 670, "李慕婉": 608, "徐立国": 580, "韩立": 688}  # key不可以重复，若重复，后面value值则会覆盖前面的值

print(dict1)
print(type(dict1))

# key必须得是不可变类型（str，int，float，tuple）, 不能是 list、set、dict
dict2 = {0: 670, 1.5: 608, (1, 2): 580, ('A', 'B'): 688}
print(dict2)

# 访问
value_1 = dict1["李慕婉"]  # 根据键获取值
print(value_1)
dict1["李慕婉"] = 688  # 根据键修改值
print(dict1)
