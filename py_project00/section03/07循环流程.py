"""
for循环的一个轮询遍历机制，对一批内容进行逐个访问
todo:本质是就是一个迭代器
后面也可以接else（可选）
"""
msg = "Hello_Python"
count = 0
for element in msg:
    print(f"第{count + 1}个字符是{element}")
    count += 1
else:
    print(f"msg里包含{count}个字符")
    print("循环正常结束")
