'''
1，input

2，检测input数据类型str

3，int()转换数据类型

4，检查是否转换成功

'''

num = input('请输入数字：')
type(num)
print(type(num))
print('您输入的数字是%s' % num)

int(num)  # 把输入的num转化成整数型
print(type(int(num)))
print('您输入的数字是%s' % num)

