# 修改
# 修改指定下标数据

name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'aaa'
# 结果：['aaa', 'Lily', 'Rose']
print(name_list)
# 第一种，直接让列表的第某位数据等于多少，跟c语言里面的数组一样的意思

# 逆置：reverse()
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
# 结果：[8, 6, 3, 2, 5, 1]
print(num_list)
# 换顺序，前变后，后变前

# 排序：sort()
# 语法：列表序列.sort( key=None, reverse=False)
# 注意：reverse表示排序规则，reverse = True 降序， reverse = False 升序（默认）
num_list = [1, 5, 2, 3, 6, 8]
num_list.sort()  # 就是默认的把列表里面的数据按从小到大的顺序重新排列
# 结果：[1, 2, 3, 5, 6, 8]
print(num_list)

