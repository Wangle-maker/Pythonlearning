# 拆包和交换变量值
'''拆包'''

# 拆包：元组
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)  # 100
print(num2)  # 200

# 拆包：字典
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1
# 对字典进⾏拆包，取出来的是字典的key
print(a)  # name
print(b)  # age
print(dict1[a])  # TOM
print(dict1[b])  # 18

'''交换变量值'''
# 需求：有变量 a = 10 和 b = 20 ，交换两个变量的值。
# ⽅法⼀:借助第三变量存储数据。
# 1. 定义中间变量
c = 0
# 2. 将a的数据存储到c c = a
# 3. 将b的数据20赋值到a，此时a = 20
a = b
# 4. 将之前c的数据10赋值到b，此时b = 10
b = c
print(a)  # 20
print(b)  # 10

# ⽅法⼆:
a, b = 1, 2
a, b = b, a
print(a)  # 2
print(b)  # 1
