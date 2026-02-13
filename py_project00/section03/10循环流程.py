"""
真尼玛绝
"""

correct_username = "admin"
correct_password = "q1234567"

while True:
    name = input("请输入用户名")
    password = input("请输入用户密码")
    if name == "" or password == "":
        password = input("请输入用户密码")
        continue  # 本次循环的代码终结点
    elif password == correct_password and name == correct_username:
        print("登陆成功")
        break
    else:
        print("用户名或密码错误，请重新输入")
