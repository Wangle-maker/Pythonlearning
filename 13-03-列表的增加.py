# 增加

# append()作⽤：增加指定数据到列表中。
#       语法：列表序列.append(数据)
# extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。
#       语法：列表序列.extend(数据)
# insert()：指定位置新增数据。
#       语法：列表序列.insert(位置下标, 数据)

name_list = ['Tom', 'Lily', 'Rose']
print(name_list)
name_list.append('xiaoming')
# 结果：['Tom', 'Lily', 'Rose', 'xiaoming']
print(name_list)
# 列表追加数据的时候，直接在原列表⾥⾯追加了指定数据，即修改了原列表，故列表为可变类型数据。
# 注意点 如果append()追加的数据是⼀个序列，则追加整个序列到列表
name_list = ['Tom', 'Lily', 'Rose']
print(name_list)
name_list.append(['xiaoming', 'xiaohong'])
name_list.append(['xiaozhang', 'xiaohua'])
# 结果：['Tom', 'Lily', 'Rose', ['xiaoming', 'xiaohong'], ['xiaozhang', 'xiaohua']]
print(name_list)


# 单个数据
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('xiaoming')
# 结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
print(name_list)
# 序列数据
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend(['xiaoming', 'xiaohong'])
# 结果：['Tom', 'Lily', 'Rose', 'xiaoming', 'xiaohong']
print(name_list)


name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1, 'xiaoming')
# 结果：['Tom', 'xiaoming', 'Lily', 'Rose']
print(name_list)
