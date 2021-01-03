
"""
需求：进⼊系统显示系统功能界⾯，功能如下：
    添加学员
    删除学员
    修改学员信息
    查询学员信息
    显示所有学员信息
    退出系统
系统共6个功能，⽤户根据⾃⼰需求选取。"""

"""
1. 显示功能界⾯
2. ⽤户输⼊功能序号
3. 根据⽤户输⼊的功能序号，执⾏不同的功能(函数)
3.1 定义函数
3.2 调⽤函数"""


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
    zengjia_dict = {}
    x = 0
    while x <= 3:
        if x == 0:
            zengjia_dict['姓名'] = input('请输入学员姓名信息:')
        elif x == 1:
            zengjia_dict['学号'] = input('请输入学员学号信息:')
        elif x == 3:
            zengjia_dict['宿舍号'] = input('请输入学员宿舍号信息:')
        x += 1
    xinxi.append(zengjia_dict)
    print(xinxi)


# for a in range(len(xinxi_list)):
# 	print(xinxi_list[a])


def panduan():
    """判断学学员信息是否存在"""
    j = 0
    for i in range(0, len(xinxi)):
        if b not in xinxi[i].values():
            j += 1
        i += 1
    if j < len(xinxi):
        return 1
    else:
        return 0


def shanchu():
    """删除学员函数"""
    for i in range(0, len(xinxi)):
        if b in xinxi[i].values():
            del xinxi[i]
            break
        else:
            i += 1


def xiugai():
    """修改学员信息函数"""
    for i in range(0, len(xinxi)):
        if b in xinxi[i].values():
            xinxi[i]['姓名'] = input('请输入修改后的姓名:')
            xinxi[i]['学号'] = input('请输入修改后的学号:')
            xinxi[i]['宿舍号'] = input('请输入修改后的宿舍号:')


def chaxun():
    """查询学员信息函数"""
    for i in range(0, len(xinxi)):
        if b in xinxi[i].values():
            print(f'要查询的学员信息地址下标是{i}\n查询结果是{xinxi[i]}')


def xianshi():
    """显示学员信息函数（显示全部学员信息）"""
    for key in xinxi[0].keys():
        print(key, end='\t\t\t')
    print()
    for i in range(0, len(xinxi)):
        for j in xinxi[i].values():
            print(j, end='\t\t\t')
        print()


chushihua()  # 输入指令，判断，并执行相应动作
zhiling = int(input('您要进行的指令是：'))  # 输入的指令都是str类型，但是需要的是int类型，用类型转换函数转换成需要的类型
xinxi = [{'姓名': '11', '学号': '11', '宿舍号': '11'}, {'姓名': '111', '学号': '111', '宿舍号': '111'}, {'姓名': '1111', '学号': '1111', '宿舍号': '1111'}]  # 创建空列表用来存储学员信息，信息包括姓名，学号，宿舍号。

# 用while循环来执行操作
while 1:
    """增加学员信息函数"""
    if zhiling == 1:
        b = input('请输入学员信息，来判断学员信息是否存在：')
        if panduan():
            print('学员信息已经存在')
        else:
            print('学员信息不存在，请继续操作来添加学员信息')
            zengjia()
        print('是否还需要添加学员信息？')
        print('1 = 继续添加')
        print('2 = 停止添加，返回主菜单')
        caozuo: int = int(input('请输入1或2来执行相应操作:'))
        if caozuo == 1:
            zhiling = 1
        elif caozuo == 2:
            chushihua()
            zhiling = int(input('您要进行的指令是：'))
        else:
            print('输入错误，请重新输入')
            continue

    """删除学员信息函数"""
    if zhiling == 2:
        b = input('请输入学员的学号信息，来判断学员信息是否存在：')
        if panduan():
            print('学员信息存在,是否确认执行删除指令')
            if input('1或0进行选择，1是确认，0是取消:'):
                shanchu()
                print(xinxi)
                print('学员信息已经删除')
                print('是否还需要删除学员信息？')
                print('1 = 继续删除')
                print('2 = 停止删除，返回主菜单')
                caozuo = int(input('请输入1或2来执行相应操作:'))
                if caozuo == 1:
                    zhiling = 2
                elif caozuo == 2:
                    chushihua()
                    zhiling = int(input('您要进行的指令是：'))
                else:
                    print('输入错误，请重新输入')
                    continue
            else:
                zhiling = 2
        else:
            print('学员信息不存在，请确认学员信息后再操作或返回主菜单')
            if input('1或0进行选择，1是重新输入，0是返回主菜单:'):
                zhiling = 2
            else:
                chushihua()
                zhiling = int(input('您要进行的指令是：'))

    """修改学员信息函数"""
    if zhiling == 3:
        b = input('请输入学员的学号信息，来判断学员信息是否存在：')
        if panduan():
            print('学员信息存在,是否确认执行修改指令')
            if input('1或0进行选择，1是确认，0是取消:'):
                xiugai()
                print('学员信息已经修改')
                print('是否还需要修改学员信息？')
                print('1 = 继续修改')
                print('2 = 停止修改，返回主菜单')
                caozuo = int(input('请输入1或2来执行相应操作:'))
                if caozuo == 1:
                    zhiling = 3
                elif caozuo == 2:
                    chushihua()
                    zhiling = int(input('您要进行的指令是：'))
                else:
                    print('输入错误，请重新输入')
                    continue

    """查询学员信息函数"""
    if zhiling == 4:
        b = input('请输入学员的学号信息，来判断学员信息是否存在：')
        if panduan():
            print('学员信息存在,查询结果如下:')
            chaxun()
            print('是否还需要查询其他学员信息？')
            print('1 = 继续查询')
            print('2 = 停止查询，返回主菜单')
            caozuo = int(input('请输入1或2来执行相应操作:'))
            if caozuo == 1:
                zhiling = 4
            elif caozuo == 2:
                chushihua()
                zhiling = int(input('您要进行的指令是：'))
            else:
                print('输入错误，请重新输入')
                continue

    """显示学员信息函数（显示全部学员信息）"""
    if zhiling == 5:
        xianshi()
        print('学员信息显示如上')
        b = input('按Enter退出显示，回到主菜单')
        if b == 0:
            chushihua()
            zhiling = int(input('您要进行的指令是：'))
        else:
            chushihua()
            zhiling = int(input('您要进行的指令是：'))

    """退出系统函数"""
    if zhiling == 6:
        chushihua()
        zhiling = int(input('您要进行的指令是：'))
