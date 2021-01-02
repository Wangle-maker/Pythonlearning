def chushihua():
    """初始化函数"""
    print('您好，欢迎进入学员管理系统：\n请输入相应的指令进行相应的操作')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')


def zengjia():
    """增加学员函数"""
    print('欢迎进入添加学员操作，请按提示操作添加学员信息')
    zengjia_list = [0, 0, 0]
    j = 0
    while j <= 3:
        if j == 0:
            zengjia_list[0] = input('请输入学员姓名信息:')
        elif j == 1:
            zengjia_list[1] = input('请输入学员学号信息:')
        elif j == 3:
            zengjia_list[2] = input('请输入学员宿舍号信息:')
        j += 1
    xinxi_list.append(zengjia_list)
    print(xinxi_list)


# for a in range(len(xinxi_list)):
# 	print(xinxi_list[a])


def panduan():
    """判断学学员信息是否存在"""
    b = input('请输入学员信息，来判断学员信息是否存在：')
    j = 0
    for i in range(0, len(xinxi_list)):
        if b not in xinxi_list[i]:
            j += 1
        i += 1
    print(f'{j}')
    if j < len(xinxi_list):
        print('学员信息已经存在')
    else:
        print('学员信息不存在，请继续操作来添加学员信息')
        zengjia()


chushihua()  # 输入指令，判断，并执行相应动作
zhiling = int(input('您要进行的指令是：'))  # 输入的指令都是str类型，但是需要的是int类型，用类型转换函数转换成需要的类型
xinxi_list = [['姓名', '学号', '宿舍号']]  # 创建空列表用来存储学员信息，信息包括姓名，学号，宿舍号。

# 用while循环来执行操作
while 1:
    """增加学员信息函数"""
    if zhiling == 1:
        panduan()
        print('是否还需要添加学员信息？')
        print('1 = 继续添加')
        print('2 = 停止添加，返回主菜单')
        caozuo = int(input('请输入1或2来执行相应操作:'))
        if caozuo == 1:
            zhiling = 1
        elif caozuo == 2:
            chushihua()
            zhiling = int(input('您要进行的指令是：'))
        else:
            print('输入错误，请重新输入')
            continue
