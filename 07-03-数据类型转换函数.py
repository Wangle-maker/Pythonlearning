'''

    int(x [,base ]) 将x转换为⼀个整数
    float(x ) 将x转换为⼀个浮点数
    complex(real [,imag ]) 创建⼀个复数，real为实部，imag为虚部
    str(x ) 将对象 x 转换为字符串
    repr(x ) 将对象 x 转换为表达式字符串
    eval(str ) ⽤来计算在字符串中的有效Python表达式,并返回⼀个对象
    tuple(s ) 将序列 s 转换为⼀个元组
    list(s ) 将序列 s 转换为⼀个列表
    chr(x ) 将⼀个整数转换为⼀个Unicode字符
    ord(x ) 将⼀个字符转换为它的ASCII整数值
    hex(x ) 将⼀个整数转换为⼀个⼗六进制字符串
    oct(x ) 将⼀个整数转换为⼀个⼋进制字符串
    bin(x ) 将⼀个整数转换为⼀个⼆进制字符串

'''
# 1. float() -- 转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))


# 2. str() -- 转换成字符串类型
num2 = 10
print(type(str(num2)))


# 3. tuple() -- 将⼀个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))


# 4. list() -- 将⼀个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))


# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

