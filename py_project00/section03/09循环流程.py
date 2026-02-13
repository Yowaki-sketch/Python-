"""
嵌套循环
"""

# 1.接受键盘录入
# m = int(input("请输入长度"))
#
# n = int(input("请输入宽度"))


# 2.打印矩形
# for i in range(m):
#     for j in range(n):
#         print("*", end=" ")
#     print()
#
# while版
print("while循环版")
num1 = 1
while num1 < 10:
    num2 = 1
    while num2 < num1 + 1:
        print(f"{num1} × {num2} = {num1 * num2}", end="\t")
        num2 += 1
    num1 += 1
    print()

# for版
print("for循环版")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
