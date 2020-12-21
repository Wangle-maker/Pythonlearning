# 字符串是 Python 中最常⽤的数据类型。我们⼀般使⽤引号来创建字符串。创建字符串很简单，只要为变量分配⼀个值即可。

a = 'hello world'
b = "abcdefg"
print(type(a))
print(type(b))

# 注意：三引号形式的字符串⽀持换⾏。

name3 = ''' Tom '''
name4 = """ Rose """
a = ''' i am Tom,
    nice to meet you! '''
b = """ i am Rose,
    nice to meet you! """
print(f'{a}')
print(f'{b}')

# 如果创建⼀个字符串 I'm Tom ?
c = "I'm Tom"
d = 'I\'m Tom'
print(f'{c}')
print(f'{d}')

name = input('请输入您的名字：')
print(f'您的名字是：{name}')

# “下标” ⼜叫 “索引” ，就是编号。⽐如⽕⻋座位号，座位号的作⽤：按照编号快速找到对应的座位。同理，下标的作⽤即是通过下标快速找到对应的数据。
name = "abcdef"
print(name[1])
print(name[0])
print(name[2])
# 注意：下标从0开始。

"""
    切⽚是指对操作的对象截取其中⼀部分的操作。字符串、列表、元组都⽀持切⽚操作。
    1. 不包含结束位置下标对应的数据， 正负整数均可；
    2. 步⻓是选取间隔，正负整数均可，默认步⻓为1。
"""
name = "abcdefg"
print(name[2:5:1])  # cde
print(name[2:5])  # cde , 默认步⻓为1。
print(name[:5])  # abcde, 默认从0开始。
print(name[1:])  # bcdefg,  不写结束位置就是直接从标定的开头到结尾。
print(name[:])  # abcdefg,  都不写就是输出全部的数据
print(name[::2])  # aceg,   第三个位置是步长
print(name[:-1])  # abcdef, 负1表示倒数第⼀个数据
print(name[-4:-1])  # def
print(name[::-1])  # gfedcba,   步长是负数就是从最后一个往前来
# print(name[初始位置：结束位置（但是不包括这个位置，和range函数一样）：步长（）可以是负数，就是反过来走])
