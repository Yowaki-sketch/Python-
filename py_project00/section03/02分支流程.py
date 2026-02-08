"""
Python特色：
TODO:缩进在Python里是一个很重要的语法

"""
correct_account = "1728908221"
correct_password = "q1234567"
account = input("请输入登录账号")
password = input("请输入登录账号")
if account == correct_account and password == correct_password:
    print("登录成功")
    print("您已进入页面")
else:
    print("登陆失败，账号或密码错误")
