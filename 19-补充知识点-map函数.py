"""
用map( ) ， split( )以及input( ) 可以实现用input( )同时输入多个数。

1.map( )
    map()函数接收两个参数，一个是函数，一个是序列，
    map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

2.split( )
    拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）

3.map(function,input(“以空格分开”).split())
    由于input( )输出的是用空格分开的字符串，split( )会分割开各个值并放到列表中，
    此时在列表中的值是字符串，如果要用于运算必须在map( )中利用int( )或者float( )等处理，再赋值。
    如果需要赋值的值都是字符串的话就没必要用map函数了。
"""
# python中的输入raw_input只能读入一个数，但
# 是有时候需要读入多个数，我们该怎么办呢，读两个数可以使用两个raw_input，但是我们如果需要读取十个数怎么办，不能使用十个raw_nput 吧。
import sys
num1, num2 = map(int, sys.stdin.readline().split())  # 它主要是切割字符串，结果返回由字符串元素组成的一个列表，具体怎么使用看下面的代码。
print(num1, num2)
# 如果需要理解上面的代码我们需要知道map函数的用法和作用，懂了之后再看下面的代码简直就是so easy啊。


# 1、对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
def add100(x):
    return x + 100


hh = [11, 22, 33]
map(add100, hh)
# 输出：[111, 122, 133]


# 2.如果map调用的函数需要多个参数，也可以传入多个参数。
def abc(a, b, c):
    return a * 10000 + b * 100 + c


list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]
map(abc, list1, list2, list3)
# 输出为：[114477, 225588, 336699]

# 3.如果'function'给出的是‘None’，会将传入的参数变成一个含有几个元组的列表。
# <pre name="code" class="python">
list1 = [11, 22, 33]
map(None, list1)
# 输出为：[11, 22, 33]
list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]
map(None, list1, list2, list3)
# 输出为：[(11, 44, 77), (22, 55, 88), (33, 66, 99)]
"""
map(f, iterable)
基本上等于：
[f(x) for x in iterable]"""


# 例子：
def add100(x):
    return x + 100


list1 = [11, 22, 33]
map(add100, list1)
# 输出为：[101, 102, 103]

[add100(i) for i in list1]


# 输出为：[101, 102, 103]

def abc(a, b, c):
    return a * 10000 + b * 100 + c


list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]
map(abc, list1, list2, list3)
# 输出为：[114477, 225588, 336699]

[abc(a, b, c) for a, b, c in zip(list1, list2, list3)]
# 输出为：[114477, 225588, 336699]
