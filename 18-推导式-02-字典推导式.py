# 字典推导式
"""
思考：如果有如下两个列表：
    list1 = ['name', 'age', 'gender']
    list2 = ['Tom', 20, 'man']
如何快速合并为⼀个字典？
答：字典推导式
字典推导式作⽤：快速合并列表为字典或提取字典中⽬标数据。"""

# 创建⼀个字典：字典key是1-5数字，value是这个数字的2次⽅。
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}

# 将两个列表合并为⼀个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

# 提取字典中⽬标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量⼤于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)  # {'MBP': 268, 'DELL': 201}

