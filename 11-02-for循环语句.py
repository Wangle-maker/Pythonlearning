"""
    for 临时变量 in 序列:
     重复执⾏的代码1
     重复执⾏的代码2
     ......
"""

str1 = 'itheima'
for i in str1:
    print(i)

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)

# 循环可以和else配合使⽤，else下⽅缩进的代码指的是当循环正常结束之后要执⾏的代码
i = 0
for i in range(4):
    if i <= 4:
        print('媳妇儿，我错了')
else:
    print('媳妇儿原谅我了')

# for
    # range函数生成一个等差级数链表，比如range(10)生成从0到9的整数，注意，如果只有一个参数，则这个参数为右边界，则左边界默认为0，右边界取不到，而和c语言中for循环的停止条件一般使用<或>而不用≤或大于等于
    """// C语言for循环
    // i取0到9
    for (int i=0;i < 10;i++)
        {
            ...
        }"""
    """# Pythonfor循环
    # i取0到9
    for i in range(10):
        ..."""
# len
    # for循环很多时候用来遍历，一般都会由界限，例如便利一个列表时，需要获取列表的长度，则len函数可以达到此效果，然后配合for循环和range函数就可以成功便利
    """a = [1, 2, 3, 4]
    for i in range(len(a)):
        print(a[i])
        # 亦可写成下面的形式
        # for i in a:
        print(i)"""
for i in range(2, 10):
    print(f'{i}')

# 冒号
    # 不难注意到第一句后面永远有一句冒号，至于作用，可以理解为解释说明，几乎在所有具有内嵌语句的结构的首句的末端都有一个冒号，比如定义函数def，for循环，while，do while，if判断等等
