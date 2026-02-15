"""
字符串：字符的容器
可以存储任数量的字符
1.不可变
2.有序性：有索引
3.可迭代性：可以用for(迭代器)遍历
todo:可以用切片操作，切片后生成的对象仍为字符串
todo:切片细节补充：需要索引方向和补偿方向一致
"""

mojis = "son-of-bitch"

print(mojis[2])  # n
print(mojis[-2])  # c

# moji[4] = "A" # 字符串不可变
# 可迭代
for moji in mojis:
    print(moji, end=" ")

# 切片操作
mojis_piece = mojis[7::1]
mojis_piece2 = mojis[7::-1]  # 步长为负，从后往前取（做因包后不包前）
print(mojis_piece)
print(mojis_piece2)

mojis_piece3 = mojis[7:1:1]  # todo：步长为正->如果起始索引大于于结束索，引切片则为空,起始和结束索引相等也为空
mojis_piece4 = mojis[1:7:-2]  # todo:步长为负->如果起始索引小于结束索，引切片则为空
print("第三个切片的内容是:", mojis_piece3)
print("第4个切片的内容是:", mojis_piece4)
