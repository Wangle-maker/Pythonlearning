
# 增

# 写法：字典序列[key] = 值
# 注意：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。

# 但是有一个需要注意的地方是，最好不要用下面的代码来给字典增加新的键值对，会报错，原因是上面你已经新建了dict1的字典，下面相当于也是一个定义，冲突了
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name'] = 'Rose'
print(dict1)  # 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}

# 正确的做法是用setdefault函数来给字典增添新的键值对。对应的修改如下：
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1.setdefault('name', 'Rose')
print(dict1)  # 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}

dict1['id'] = 110
# {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
print(dict1)

# 删

# del() / del：删除字典或删除字典中指定键值对。
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1)  # 结果：{'name': 'Tom', 'age': 20}

# clear()：清空字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1.clear()
print(dict1)  # {}

# 改
# 写法：字典序列[key] = 值
# 注意：如果key存在则修改这个key对应的值 ；如果key不存在则新增此键值对。

# 查
#      key值查找
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])  # Tom
# print(dict1['id'])  # 报错
# 如果当前查找的key存在，则返回对应的值；否则则报错。

# get()
# 语法:字典序列.get(key, 默认值)
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))  # Tom
# 注意：如果当前查找的key不存在则返回第⼆个参数(默认值)，如果省略第⼆个参数，则返回None。
print(dict1.get('id', 110))  # 110
print(dict1.get('id'))  # None

# keys()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])

# values()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.values())  # dict_values(['Tom', 20, '男'])

# items()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])




