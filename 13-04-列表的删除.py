# 删除

# del
# 语法：del 目标

"""# 删除列表
name_list = ['Tom', 'Lily', 'Rose']
# 结果：报错提示：name 'name_list' is not defined
del name_list
print(name_list)
"""

# 删除指定数据
name_list = ['Tom', 'Lily', 'Rose']
del name_list[0]
# 结果：['Lily', 'Rose']
print(name_list)

# pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据。
# 语法：列表序列.pop(下标)
name_list = ['Tom', 'Lily', 'Rose']
del_name = name_list.pop(1)
# 结果：Lily
print(del_name)
# 结果：['Tom', 'Rose']
print(name_list)

name_list = ['Tom', 'Lily', 'Rose']
a = name_list.pop()
print(a)  # 默认删除最后一个数据，可以通过下标的标定来切换删除的数据，然后返回要被删除的数据
print(name_list)  # 就是删除完默认数据后的列表剩下的部分按之前的顺序排列，成为新的列表

# remove()：移除列表中某个数据的第⼀个匹配项。
# 语法：列表序列.remove(数据)
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
# 结果：['Tom', 'Lily']
print(name_list)  # 删除列表里面第一个跟指定数据相同的数据
name_list = ['Tom', 'Lily', 'Rose', 'sis', 'Rose']
name_list.remove('Rose')  # remove命令不返回任何东西，执行了之后列表里面的东西就已经被删除了
print(name_list)


# clear()：清空列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.clear()
print(name_list)  # 结果： []
