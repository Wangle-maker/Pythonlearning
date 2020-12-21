# 所谓判断即是判断真假，返回的结果是布尔型数据类型：True 或 False。

# startswith()：检查字符串是否是以指定⼦串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
# 语法：字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标)
mystr = "hello world and itcast and itheima and Python "
print(mystr.startswith('hello'))  # 结果：True
# 查看字符串是不是以你指定的字符串开始，是就返回1，不是就返回0
print(mystr.startswith('hello', 5, 20))  # 结果False
# 同上，在第5个字符开始到第20个字符结束的范围内，看看是不是一指定字符串开始，是就是返回1，不是就返回0

# endswith()：：检查字符串是否是以指定⼦串结尾，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
# 语法： 字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标)
mystr = "hello world and itcast and itheima and Python"
print(mystr.endswith('Python'))  # 结果：True
print(mystr.endswith('python'))  # 结果：False
# 判断
print(mystr.endswith('Python', 2, 20))  # 结果：False
# 指定范围内判断

# isalpha()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟则返回 True, 否则返回 False。
mystr1 = 'hello'
mystr2 = 'hello12345'
print(mystr1.isalpha())  # 结果：True
# 字符串不是空的而且全部是由字母组成的就返回1，不然就返回0
print(mystr2.isalpha())  # 结果：False
# 这个同上，因为包含数字所以返回了0

# isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
mystr1 = 'aaa12345'
mystr2 = '12345'
print(mystr1.isdigit())  # 结果： False
print(mystr2.isdigit())  # 结果：False

# isalnum()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟或数字则返 回 True,否则返回 False。
mystr1 = 'aaa12345'
mystr2 = '12345-'
print(mystr1.isalnum())  # 结果：True
print(mystr2.isalnum())  # 结果：False

# isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False。
mystr1 = '1 2 3 4 5'
mystr2 = ' '
print(mystr1.isspace())  # 结果：False
print(mystr2.isspace())  # 结果：True
