# 当程序执⾏到 input ，等待⽤户输⼊，输⼊完成之后才继续向下执⾏。
# 在Python中， input 接收⽤户输⼊后，⼀般存储到变量，⽅便使⽤。
# 在Python中， input 会把接收到的任意⽤户输⼊的数据都当做字符串处理。

'''
1.书写input('提示信息')

2,观察特点
    遇到input，等待用户输入
    接受input存变量
    input接受到的数据类型都是字符串
'''

password = input('请输入您的密码：')
print('您輸入的密碼是：%s' % password)
