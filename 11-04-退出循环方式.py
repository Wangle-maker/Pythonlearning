# 1. break终⽌循环

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print('i')
else:
    print('循环正常结束之后执⾏的代码')
# 没有执⾏else缩进的代码。

# 2. continue控制循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
# 因为continue是退出当前⼀次循环，继续下⼀次循环，所以该循环在continue控制下是可以正常
# 结束的，当循环结束后，则执⾏了else缩进的代码。

"""
循环的作⽤：控制代码重复执⾏

while语法
    while 条件:
        条件成⽴重复执⾏的代码1
        条件成⽴重复执⾏的代码2
        ......

while循环嵌套语法
    while 条件1:
        条件1成⽴执⾏的代码
        ......
        while 条件2:
            条件2成⽴执⾏的代码
            ......
            
for循环语法
    for 临时变量 in 序列:    序列用range()函数实现，range(1,4),表示从1到4，包括1，如果1的位置不写东西就是从0开始包括0，比如range（5）就是从0开始但是小于5，就是0,1,2,3,4一共5个数
        重复执⾏的代码1
        重复执⾏的代码2
        ......
        
break退出整个循环

continue退出本次循环，继续执⾏下⼀次重复执⾏的代码

else
    while和for都可以配合else使⽤
    else下⽅缩进的代码含义：当循环正常结束后执⾏的代码
    break终⽌循环不会执⾏else下⽅缩进的代码
    continue退出循环的⽅式执⾏else下⽅缩进的代码
    
"""