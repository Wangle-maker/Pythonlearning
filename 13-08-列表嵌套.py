# 列表嵌套
# 所谓列表嵌套指的就是⼀个列表⾥⾯包含了其他的⼦列表

# 应⽤场景：要存储班级⼀、⼆、三三个班级学⽣姓名，且每个班级的学⽣姓名在⼀个列表。
name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
# print(name_list[0][2])
# 思考： 如何查找到数据"李四"？
i = 0
j = 0
k = 0
while i < len(name_list):
    for j in name_list[i]:
        if j == '李四':
            k = name_list[i].index('李四')
            print(f'李四所在的位置是{i+1},{k+1}')
    i += 1


# 第⼀步：按下标查找到李四所在的列表
print(name_list[2])
# 第⼆步：从李四所在的列表⾥⾯，再按下标找到数据李四
print(name_list[2][1])
