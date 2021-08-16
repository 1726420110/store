
# 编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数
def cacluate(*n):
    x = sum(n)/len(n)
    round(x,2)
    y = []
    for i in n:
        if i > x:
            y.append(i)
    a = (x,y)
    return a

# 编写函数, 接收一个列表和一个索引，返回这个列表中对应索引的数据，如果索引超出范围，返回-1
def getnum(a,b):
    for i in range(len(a)):
        if a[i][0] == b:
            return a[i]

    return -1




# 不使用for或者while循环，就使用方法完成1~150之间的数的打印。（方法的递归调用）
def d1_150(i):
    if i < 151:
        print(i)
        i += 1
        d1_150(i)
def i():
    i = 1
    d1_150(i)


# 同样使用方法的递归，求1~300所有数的和。
def s1_300(i,s):
    if i < 301:
        s = s + i
        i = i + 1
        s = s1_300(i,s)
    return s

def a():
    a = 1
    sum = 0
    sum = s1_300(a,sum)
    print(sum)

def xuanke():
    # 用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
    chinese = ['明','华','红','张','李']
    math = ['陈','华','张','羽','索']
    english = ['明','李','陈','索','红']
    # 1) 求选课学生总共有多少人
    k = chinese + math + english
    b = len(set(k))
    print(b)
    # 2) 求只选了第一个学科的人的数量和对应的名字
    print(len(chinese))
    for i in chinese:
        print(i,end = " ")
    print("")
    # 3) 求只选了一门学科的学生的数量和对应的名字
    x1 = []
    for i,v in enumerate(k):
        if v in k[:i]:
            continue
        if k.count(v) == 1:
            x1.append(v)
            print(len(x1),v)






# 编程实现9x9乘法表
def b9x9():
    for i in range(9,0,-1): #   i,由9－》0
        for j in range(1,i+1):  #   j，由0－》9
            print(j,"x",i,"=",i*j,end="  ")
        print()

