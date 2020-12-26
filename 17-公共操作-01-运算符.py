# 运算符

"""运算符          描述             ⽀持的容器类型
    +             合并            字符串、列表、元组
    *             复制            字符串、列表、元组
    in            元素是否存在      字符串、列表、元组、字典
    not in        元素是否不存在    字符串、列表、元组、字典
"""

# + 合并
# 1. 字符串
str1 = 'aa'
str2 = 'bb'
str3 = str1 + str2
print(str3)  # aabb
# 2. 列表
list1 = [1, 2]
list2 = [10, 20]
list3 = list1 + list2
print(list3)  # [1, 2, 10, 20]
# 3. 元组
t1 = (1, 2)
t2 = (10, 20)
t3 = t1 + t2
print(t3)  # (10, 20, 100, 200)

# * 复制
# 1. 字符串
print('-' * 10)  # ----------
# 2. 列表
list1 = ['hello']
print(list1 * 4)  # ['hello', 'hello', 'hello', 'hello']
# 3. 元组
t1 = ('world',)
print(t1 * 4)  # ('world', 'world', 'world', 'world')

# in或not in
# 1. 字符串
print('a' in 'abcd')  # True
print('a' not in 'abcd')  # False
# 2. 列表
list1 = ['a', 'b', 'c', 'd']
print('a' in list1)  # True
print('a' not in list1)  # False
# 3. 元组
t1 = ('a', 'b', 'c', 'd')
print('aa' in t1)  # False
print('aa' not in t1)   # True

