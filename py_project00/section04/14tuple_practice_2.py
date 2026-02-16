"""
用元组列表模仿对象的案例
"""
# 录入学生对象
students = (
    ("S000", "王琳", 85, 89, 78),
    ("S001", "李默", 92, 88, 86),
    ("S002", "十三", 77, 85, 82),
    ("S003", "碧池", 88, 79, 91),
    ("S004", "前锋", 95, 96, 89),
    ("S005", "钢门吹雪", 76, 80, 77),
    ("S006", "周芷若", 89, 91, 94),
    ("S007", "金庸", 75, 69, 81),
    ("S008", "笔笔", 86, 98, 77),
    ("S009", "小白", 99, 96, 59),
)
# 1.计算每个学生的总成绩
for stu in students:
    total = stu[2] + stu[3] + stu[4]
    avg = total / 3
    print(f"学号为{stu[0]}的学生:{stu[1]},总分为{total},平均分数为%.2f" % avg)
    print(f"学号为{stu[0]}的学生:{stu[1]},总分为{total},平均分数为{avg:.1f}")  # todo:f快速格式化也可以指定输出格式

print("==============================================")

# 2.统计各科的最低分最高分平均分
# 用列表推导式得到每科成绩的列表
chinese_score = [stu[2] for stu in students]
math_score = [stu[3] for stu in students]
en_score = [stu[4] for stu in students]
print(
    f"语文的最高分为{max(chinese_score)}，最得分为{min(chinese_score)}，平均分为{sum(chinese_score) / len(chinese_score):.1f}")
print(f"数学的最高分为{max(math_score)}，最得分为{min(math_score)}，平均分为{sum(math_score) / len(math_score):.1f}")
print(f"语文的最高分为{max(en_score)}，最得分为{min(en_score)}，平均分为{sum(en_score) / len(en_score):.1f}")
print("==============================================")

# 3.查找出平均分大于90分的优秀学生
for stu in students:
    total = stu[2] + stu[3] + stu[4]
    avg = total / 3
    if avg > 90:
        print(f"学号为{stu[0]}的学生：{stu[1]}，平均分为{avg:.1f}")
