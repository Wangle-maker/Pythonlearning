# 打印图形

# 1. 打印⼀条横线
def print_line():
    print('-' * 20)


print_line()


# 2. 打印多条横线
def print_line():
    print('-' * 20)


def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)


# 函数计算
# 1. 求三个数之和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
print(result)  # 6


# 2. 求三个数平均值
def average_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


result = average_num(1, 2, 3)
print(result)  # 2.0
