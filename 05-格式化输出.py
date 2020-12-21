'''
1，准备数据
2，格式化符号输出数据
'''

age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000
# 我今年年龄是x岁   整数--%d
print('我的年龄是%d岁')
print('我的年龄是%d岁' % age)

# 我的名字是x   字符串--%s
print('我的名字是%s' % name)
print('我的名字是%s' % '王徐泳')

# 我的体重是x公斤  浮点数--%f
print('我的体重是%f公斤' % weight)
print('我的体重是%.2f公斤' % weight)  # 保留几位小数，小数点后面写几,%.2f，表示⼩数点后显示的⼩数位数。

# 我的学号是x
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)  # %06d，表示输出的整数显示位数，不⾜以0补全，超出当前位数则原样输出

# 我的名字是x，今年x岁了
print('我的名字是%s，我今年%d岁了' % (name, age))
print('我的名字是%s，我明年%d岁了' % (name, age+1))

# 我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重是%.2f公斤，学号是%03d' % (name, age, weight, stu_id))

a = 0
while a <= 4:
    print('*', end='1')
    a += 1
print('*****')
print('*****', end='')
print('*****')

print('*', end=' ')  # end值为空格
print('*', end='')  # end值为空字符串

print('*', end='')  # end值为空字符串
print('*')  # end值为默认值（换行\n）

print('*', end='1')  # end值为字符串‘1’
print('*', end='12')  # end值为字符串‘12’
