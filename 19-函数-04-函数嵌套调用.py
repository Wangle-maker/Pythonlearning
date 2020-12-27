# 函数嵌套调⽤
# 所谓函数嵌套调⽤指的是⼀个函数⾥⾯⼜调⽤了另外⼀个函数。


def testb():
    print('---- testB start----')
    print('这⾥是testB函数执⾏的代码...(省略)...')
    print('---- testB end----')


def testa():
    print('---- testA start----')
    testb()
    print('---- testA end----')


testa()

# 如果函数A中，调⽤了另外⼀个函数B，那么先把函数B中的任务都执⾏完毕之后才会回到上次函数A执⾏的位置。