# 判断是否存在
# in：判断指定数据在某个列表序列，如果在返回True，否则返回False
# not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False


# in：判断指定数据在某个列表序列，如果在返回True，否则返回False
name_list = ['Tom', 'Lily', 'Rose']
# 结果：True
print('Lily' in name_list)
# 结果：False
print('Lilys' in name_list)

# not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False
name_list = ['Tom', 'Lily', 'Rose']
# 结果：False
print('Lily' not in name_list)
# 结果：True
print('Lilys' not in name_list)


# 需求：查找⽤户输⼊的名字是否已经存在。
name_list = ['Tom', 'Lily', 'Rose']
name = input('请输⼊您要搜索的名字：')
if name in name_list:
    print(f'您输⼊的名字是{name}, 名字已经存在')
else:
    print(f'您输⼊的名字是{name}, 名字不存在')
