"""
1.按经验把不同的变量存储到不同的数据类型

2.验证这些数据到底是什么类型--检测数据类型--type（数据）

"""
# int--整型
# float--浮点型
# str--字符串，特点：通常都要带引号
# bool--布尔型
# list--列表

num1 = 1
num2 = 1.1
A = "hello,world!"
print(type(num1))
print(type(num2))
print(type(A))

# list--列表
b = [10, 20, 30]
print(type(b))

# tuple--元组
c = (10, 20, 30)
print(type(c))

# set--集合
d = {10, 20, 30}
print(type(d))

# dict--字典，键值对
f = {'name': 'TOM', 'age':18}
print(type(f))
