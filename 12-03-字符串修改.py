# 所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。
"""
    replace()：替换
    split()：按照指定字符分割字符串。
    join()：⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串。

    capitalize()：将字符串第⼀个字符转换成⼤写。
    title()：将字符串每个单词⾸字⺟转换成⼤写。

    lower()：将字符串中⼤写转⼩写。
    upper()：将字符串中⼩写转⼤写。

    lstrip()：删除字符串左侧空⽩字符。
    rstrip()：删除字符串右侧空⽩字符。
    strip()：删除字符串两侧空⽩字符。

    ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串。
    rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
    center()：返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
"""
# replace()：替换
# 语法：字符串序列.replace(旧⼦串, 新⼦串, 替换次数)
# 注意：替换次数如果超出⼦串出现次数，则替换次数为该⼦串出现次数。
mystr = "hello world and itcast and itheima and Python"
print(mystr.replace('and', 'he'))  # 结果：hello world he itcast he itheima he Python
# 把所有的and用he来替换
print(mystr.replace('and', 'he', 2))  # 结果：hello world he itcast he itheima he Python
# 把前面的两个and用he替换
print(mystr)  # 结果：hello world and itcast and itheima and Python
# 原版
"""注意：数据按照是否能直接修改分为可变类型和不可变类型两种。
    字符串类型的数据修改的时候不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型。"""


# split()：按照指定字符分割字符串。
# 语法：字符串序列.split(分割字符, num)
# 注意：num表示的是分割字符出现的次数，即将来返回数据个数为num+1个
mystr = "hello world and itcast and itheima and Python"
print(mystr.split('and'))  # 结果：['hello world ', ' itcast ', ' itheima ', ' Python']
# 用and分割字符串，但是因为and是原字符串中有的，所以丢失
print(mystr.split('and', 2))   # 结果：['hello world ', ' itcast ', ' itheima and Python']
# 用and分割字符串，而且2的意思是，只在前两个出现的位置上分割，后续出现位置不会分割
print(mystr.split(' '))  # 结果：['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']
# 同and
print(mystr.split(' ', 2))  # 结果：['hello', 'world', 'and itcast and itheima and Python']
# 同and，2
# 注意：如果分割字符是原有字符串中的⼦串，分割后则丢失该⼦串。


# join()：⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串。
# 语法：字符或⼦串.join(多字符串组成的序列)
list1 = ['chuan', 'zhi', 'bo', 'ke']
t1 = ('aa', 'b', 'cc', 'ddd')
print('_'.join(list1))      # 结果：chuan_zhi_bo_ke
# '.'句号前面的是把字符串合并起来的时候，用什么连接字符串与字符串之前的位置，这里显示的是用下划线'_'
print('...'.join(t1))       # 结果：aa...b...cc...ddd


# capitalize()：将字符串第⼀个字符转换成⼤写。
# 注意：capitalize()函数转换后，只字符串第⼀个字符⼤写，其他的字符全都⼩写。
mystr = "hello world and itcast and itheima and Python"
print(mystr.capitalize())  # 结果：Hello world and itcast and itheima and python


# title()：将字符串每个单词⾸字⺟转换成⼤写。
mystr = "hello world and itcast and itheima and Python"
print(mystr.title())  # 结果：Hello World And Itcast And Itheima And Python


# lower()：将字符串中⼤写转⼩写。
mystr = "hello world and itcast and itheima and Python"
print(mystr.lower())  # 结果：hello world and itcast and itheima and python


# upper()：将字符串中⼩写转⼤写。
mystr = "hello world and itcast and itheima and Python"
print(mystr.upper())  # 结果：HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON

mystr = "     hello world and itcast and itheima and Python     "
print(mystr)
# strip()：删除字符串两侧空⽩字符。
print(mystr.strip())
# rstrip()：删除字符串右侧空⽩字符。
print(mystr.rstrip())
# lstrip()：删除字符串左侧空⽩字符。
print(mystr.lstrip())

# ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串。
# 语法： 字符串序列.ljust(⻓度, 填充字符)
mystr = 'hello hello hello'
print(mystr.ljust(30, '.'))
print(mystr.ljust(5, '.'))
# 就是，如果字符长度不够就会用你指定的字符去补齐位数，默认用空格补齐，但是如果你指定的长度达不到原有的字符串的长度，就不会有任何改变，输出原有的字符串。
# rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
mystr = 'hello hello hello'
print(mystr.rjust(30, '.'))
print(mystr.rjust(5, '.'))
# center()：返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
mystr = 'hello hello hello'
print(mystr.center(30, '.'))
print(mystr.center(5, '.'))
