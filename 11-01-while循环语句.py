# 在Python中，循环分为 while 和 for 两种，最终实现效果相同。

"""
    while 条件:
     条件成⽴重复执⾏的代码1
     条件成⽴重复执⾏的代码2
     ......
"""
time = input('请输入循环的次数：')
i = 0
while i <= int(time):
    i += 1
    print('媳妇儿，我错了，你原谅我吧，我还是爱你的')
    if i >= int(time):
        break
print('i = %d' % i)


# 1到100自然数的和
i = 0
he = 0
while i < 100:
    i += 1
    he += i
print('和是：%d' % he)
print('i是：%d' % i)

i = 1
result = 0
while i <= 100:
    result += i
    i += 1
# 输出5050
print(result)

"""
偶数即是和2取余结果为0的数字，可以加⼊条件语句判断是否为偶数，为偶数则累加
初始值为0 / 2 , 计数器每次累加2
"""
# 计算1-100偶数累加和
i = 1
he = 0
while i <= 100:
    if i % 2 == 0:  # %是取余数，//是整除，**是次方。
        he += i
    i += 1
print('和是%d' % he)

# break和continue是循环中满⾜⼀定条件退出循环的两种不同⽅式。
"""
    举例：⼀共吃5个苹果，吃完第⼀个，吃第⼆个…，这⾥"吃苹果"的动作是不是重复执⾏？

        情况⼀：如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第五个苹果，即是吃苹果的动作
    停⽌，这⾥就是break控制循环流程，即终⽌此循环。

        情况⼆：如果吃的过程中，吃到第三个吃出⼀个⼤⾍⼦...,是不是这个苹果就不吃了，开始吃第四个苹
    果，这⾥就是continue控制循环流程，即退出当前⼀次循环继⽽执⾏下⼀次循环代码。
"""
i = 0
while i <= 5:
    i += 1
    print(f'吃了第{i}个苹果')
    if i == 4:
        print(f'吃饱了不吃了')
        break
print(f'总共吃了{i}个苹果')

j = 1
while j <= 5:
    if j == 3:
        print(f'第{j}个里面有一个⼤⾍⼦，第{j}个不吃了')
# 在continue之前⼀定要修改计数器，否则会陷⼊死循环
        j += 1
        continue
    print(f'吃了第{j}个苹果')
    j += 1

"""
    while 条件1:
      条件1成⽴执⾏的代码
      ......
      while 条件2:
      条件2成⽴执⾏的代
      ......
"""

i = 1
j = 1
while i <= 3:
    j = 1
    print(f'刷晚饭的碗第{i}天')
    i += 1
    while j <= 3:
        print('媳妇儿我错了，求求你原谅我吧，好不好呢')
        j += 1
    if i > 3:
        print('惩罚结束')


# 重复打印5⾏星星
j = 0
while j <= 4:
    #  ⼀⾏星星的打印
    i = 0
    while i <= 4:
        # ⼀⾏内的星星不能换⾏，取消print默认结束符\n
        print('*', end='')
        i += 1
    #  每⾏结束要换⾏，这⾥借助⼀个空的print，利⽤print默认结束符换⾏
    print()
    j += 1

# 分析：⼀⾏输出星星的个数和⾏号是相等的，每⾏：重复打印⾏号数字个星号，将打印⾏星号的命令重
# 复执⾏5次实现打印5⾏。
a = 0
b = 0
while a <= 4:
    a += 1
    while b < a:
        b += 1
        print('*', end='')
    print('')
    b = 0

# 重复打印5⾏星星
# j表示⾏号
j = 0
while j <= 4:
    # ⼀⾏星星的打印
    i = 0
    # i表示每⾏⾥⾯星星的个数，这个数字要和⾏号相等所以i要和j联动
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1

# 九九乘法表
a = 0
b = 0
c = 0
while a < 8:
    a += 1
    while b <= a:
        b += 1
        while c < b:
            c += 1
            print(f'{c}*{b}={c*b}', end='\t')
        c = 0
        print()


# 重复打印9⾏表达式
j = 1
while j <= 9:
    # 打印⼀⾏⾥⾯的表达式 a * b = a*b
    i = 1
    while i <= j:
        print(f'{i}*{j}={j*i}', end='\t')
        i += 1
    print()
    j += 1

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
