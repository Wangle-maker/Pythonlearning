import random
print(random.sample(range(1, 100), 10))

ran = range(10)
# 定义一个list，用来将range的范围的所有数进行陈放为list形式
arr_str = list(ran)
print(ran)
print(arr_str)

# 生成随机数列表的代码，真的强
"""
一、列表的应⽤场景
    思考：有⼀个⼈的姓名(TOM)怎么书写存储程序？
        答：变量。
    思考：如果⼀个班级100位学⽣，每个⼈的姓名都要存储，应该如何书写程序？声明100个变量吗？
        答：列表即可， 列表⼀次性可以存储多个数据。
二、 列表的格式
    列表可以⼀次性存储多个数据，且可以为不同数据类型。
        [数据1, 数据2, 数据3, 数据4......]
三、列表的常⽤操作
    列表的作⽤是⼀次性存储多个数据，程序员可以对这些数据进⾏的操作有：增、删、改、查。
"""

# 查找

# 下标
name_list = ['Tom', 'Lily', 'Rose']
print(name_list[0])  # Tom
print(name_list[1])  # Lily
print(name_list[2])  # Rose

# 函数
# index()：返回指定数据所在位置的下标 。
# 语法：列表序列.index(数据, 开始位置下标, 结束位置下标)
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.index('Lily', 0, 2))  # 1
