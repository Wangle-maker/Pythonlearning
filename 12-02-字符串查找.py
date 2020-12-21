
# 所谓字符串查找⽅法即是查找⼦串在字符串中的位置或出现的次数。
"""
    find()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则返回-1
语法：
    字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
"""
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。
mystr = "hello world and itcast and itheima and Python"
print(mystr.find('and'))  # 12，从第一个开始找是不是有对应的，有就返回对应的字符串第一个字符的下标
print(mystr.find('and', 15, 30))  # 23，从规定的位置找，找到了还是返回对应的字符串在整体字符串中的初始下标
print(mystr.find('ands'))  # -1，找不到返回-1





"""
    index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常。
语法：
    字符串序列.index(⼦串, 开始位置下标, 结束位置下标)
"""
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。
mystr = "hello world and itcast and itheima and Python"
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
print(mystr.index('ands'))  # 报错




"""
    rfind()： 和find()功能相同，但查找⽅向为右侧开始。
    rindex()：和index()功能相同，但查找⽅向为右侧开始。
"""





"""
    count()：返回某个⼦串在字符串中出现的次数
语法：
     字符串序列.count(⼦串, 开始位置下标, 结束位置下标)
"""
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。
mystr = "hello world and itcast and itheima and Python"
print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # 0
print(mystr.count('and', 0, 20))  # 1
