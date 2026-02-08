"""
利用字面量可以在代码中直接写的特性，
构成了Python的多行注释格式

"""

a = int(input("第1个边长"))
b = int(input("第2个边长"))
c = int(input("第3个边长"))

# if a + b > c and a + c > b and b + c > a:
#     pass  # todo空语句，起到一个语法占位功能，也算是Python空格语法的一种
# else:
#     print(f"{a}{c}{b}这3个边不构成三角形")

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("该三角形为等边三角形")
    elif a == b or b == c or a == c:
        print("该三角形为等腰三角形")
    else:
        print("该三角形为普通三角形")
else:
    print(f"{a}{c}{b}这3个边不构成三角形")
