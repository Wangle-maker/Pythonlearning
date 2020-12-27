# 函数的返回值

# 思考：如果⼀个函数如些两个return (如下所示)，程序如何执⾏？
def return_num():
    return 1
    return 2


result = return_num()
print(result)
# 1

# 答：只执⾏了第⼀个return，原因是因为return可以退出当前函数，导致return下⽅的代码不执⾏。
# 思考：如果⼀个函数要有多个返回值，该如何书写代码？
def return_num():
    return 1, 2


result = return_num()
print(result)
# (1, 2)
"""注意：
1. return a, b 写法，返回多个数据的时候，默认是元组类型。
2. return后⾯可以连接列表、元组或字典，以返回多个值。"""