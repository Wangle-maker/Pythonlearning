# 字典的循环遍历

# 遍历字典的key,键值对前面的
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key)


# 遍历字典的value，键值对后面的
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for value in dict1.values():
    print(value)


# 遍历字典的元素，
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for item in dict1.items():
    print(item)


# 遍历字典的键值对，
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key, value in dict1.items():
    print(f'{key} = {value}')
