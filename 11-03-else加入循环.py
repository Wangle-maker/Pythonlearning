# 循环可以和else配合使⽤，else下⽅缩进的代码指的是当循环正常结束之后要执⾏的代码
"""
    while 条件:
        条件成⽴重复执⾏的代码
    else:
        循环正常结束之后要执⾏的代码

"""
i = 1
while i <= 5:
    print('媳妇⼉，我错了')
    i += 1
else:
    print('媳妇原谅我了，真开⼼，哈哈哈哈')


"""
    for 临时变量 in 序列:
        重复执⾏的代码
         ...
    else:
        循环正常结束之后要执⾏的代码
"""

str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
