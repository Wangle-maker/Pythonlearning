
"""推导式的作⽤：简化代码
推导式写法

# 列表推导式
[xx for xx in range()]
# 字典推导式
{xx1: xx2 for ... in ...}
# 集合推导式
{xx for xx in ...}"""



# 列表推导式
"""
作⽤：⽤⼀个表达式创建⼀个有规律的列表或控制⼀个有规律列表。
列表推导式⼜叫列表⽣成式。"""

# 需求：创建⼀个0-10的列表。
"""while循环实现
for循环实现
列表推导式实现"""
# 1. 准备⼀个空列表
list1 = []
# 2. 书写循环，依次追加数字到空列表list1中
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)
# for循环实现
list1 = []
for i in range(10):
    list1.append(i)
print(list1)
# 列表推导式实现
list1 = [i for i in range(10)]
print(list1)

# 带if的列表推导式
# 需求：创建0-10的偶数列表
# ⽅法⼀：range()步⻓实现
list1 = [i for i in range(0, 10, 2)]
print(list1)
# ⽅法⼆：if实现
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# 多个for循环实现列表推导式
# 需求：创建列表如下：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 代码如下：
list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)
