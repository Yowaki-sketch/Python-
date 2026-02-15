"""
todo:字符串由于其不可变，因此调用它任何方法都不会对字符串自身产生任何修改
字符串方法
find()查找子字符串在字符串中的索引位置，返回第一个该字符串的索引位置，没有的话返回-1
count()统计字串在字符串中出现的次数
upper()将字符串中的字母转大写
lower()转小写
split(指定分割字符)分割字符串todo返回值为一个字符串数组
strip()去除字符串两边的留白或者指定todo:字符
replace()将指定的字串替换为指定的新串
startswith()检查是否已指定串开头，返回布尔值
"""

string = "hello-world-hello-python-hello-bitch"
print(string)
# 找索引
index = string.find("wo")
print(index)
# 字符串出现的次数
sum = string.count("o")
print(sum)
# 转大写
new_str = string.upper()
print(new_str)
# 转小写
new_strs = string.lower()
print(new_strs)
# 切割字符串
str_arr = string.split("-")
print(str_arr)
# 判断开头
flog1 = string.startswith("he")
flog2 = string.startswith("o0")
print(flog1, flog2)
