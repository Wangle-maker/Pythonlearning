# ⼀般在实际开发过程中，⼀个程序往往由多个函数（后⾯知识中会讲解类）组成，并且多个函数共享某些数据，如下所示：

# 共⽤全局变量
# 1. 定义全局变量
glo_num = 0


def test1():
    global glo_num
    # 修改全局变量
    glo_num = 100


def test2():
    # 调⽤test1函数中修改后的全局变量
    print(glo_num)


# 2. 调⽤test1函数，执⾏函数内部代码：声明和修改全局变量
test1()
# 3. 调⽤test2函数，执⾏函数内部代码：打印
test2()  # 100


# 返回值作为参数传递
def test1():
    return 50


def test2(num):
    print(num)


# 1. 保存函数test1的返回值
result = test1()
# 2.将函数返回值所在变量作为参数传递到test2函数
test2(result)
# 50

