"""
元素 in 容器 也可以在字符串中使用
"""

mail = input("请输入邮箱")

if mail.count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail}是格式合法的邮箱")
else:
    print(f"{mail}是格式非法的邮箱")


if mail.count("@") == 1 and "." in mail:
    print(f"{mail}是格式合法的邮箱")
else:
    print(f"{mail}是格式非法的邮箱")




