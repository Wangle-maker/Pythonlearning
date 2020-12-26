# 公共方法

"""
len()                           计算容器中元素个数
del 或 del()                     删除
max()                           返回容器中元素最⼤值
min()                           返回容器中元素最⼩值
range(start,end, step)          ⽣成从start到end的数字，步⻓为 step，供for循环使⽤
enumerate()                     函数⽤于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序列，同时列出数据和数据下标，⼀般⽤在 for 循环当中。
"""

# len()
# 1. 字符串
str1 = 'abcdefg'
print(len(str1))  # 7
# 2. 列表
list1 = [10, 20, 30, 40]
print(len(list1))  # 4
# 3. 元组
t1 = (10, 20, 30, 40, 50)
print(len(t1))  # 5
# 4. 集合
s1 = {10, 20, 30}
print(len(s1))  # 3
# 5. 字典
dict1 = {'name': 'Rose', 'age': 18}
print(len(dict1))  # 2

# # del()
# # 1. 字符串
# str1 = 'abcdefg'
# del str1
# print(str1)
# # 2. 列表
# list1 = [10, 20, 30, 40]
# del(list1[0])
# print(list1)  # [20, 30, 40]

# max()
# 1. 字符串
str1 = 'abcdefg'
print(max(str1))  # g
# 2. 列表
list1 = [10, 20, 30, 40]
print(max(list1))  # 40

# min()
# 1. 字符串
str1 = 'abcdefg'
print(min(str1))  # a
# 2. 列表
list1 = [10, 20, 30, 40]
print(min(list1))  # 10

# range()
# 注意：range()⽣成的序列不包含end数字。
for i in range(1, 10, 1):
    print(i)  # 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9
for i in range(10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9

# enumerate()
# 语法:enumerate(可遍历对象, start=0)
# 注意：start参数⽤来设置遍历数据的下标的起始值，默认为0。
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)
for index, char in enumerate(list1, start=1):
    print(f'下标是{index}, 对应的字符是{char}')
