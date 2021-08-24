import random
from bank_sql import update
from bank_sql import select

# 准备数据库和开户行名称
bank_name = "中国工商银行昌平支行"


# 登录操作
def sign_in():
    # 获取账号数据,以判断账号密码是否正确
    sql = "select account,password from bank"
    acc = select(sql)
    # 账号密码判断
    a = input("请输入您的账号:")
    for i in acc:
        if a == i[0]:
            b = input("请输入您的密码:")
            if b == i[1]:
                print("登录成功")
                return a
            else:
                print("您的密码错误")
                return 2
        else:
            print("您的账号不存在")
            return 1


# 跨行转账操作
def Super_transfer(a, b):
    # 在农行数据库查询转账账号
    sql = "select account from ny_bank"
    u1 = select(sql)
    data = []
    for i in u1:  # 遍历所有账号
        data.append(i[0])
    u1 = data  # 账号表
    if b in u1:
        s = int(input("请输入转出的金额:"))
        # 在数据库查询金额
        sql = "select money from bank where account = %s"
        param = [a]
        m = select(sql, param)
        for i in m:
            m = i[0]
        service_charge = 0
        if s <= 2000:  # 手续费计算
            service_charge = 1.6
        elif 2000 < s <= 5000:
            service_charge = 4
        elif 5000 < s <= 10000:
            service_charge = 8
        elif 10000 < s <= 50000:
            service_charge = 12
        elif s > 50000:
            service_charge = round(s * 0.0003, 2)
            if service_charge > 50:
                service_charge = 50
        if s <= m + service_charge:  # 账款计算
            # 转出账号减去转出额
            sql = "update bank set money = money  - %s - %s where account = %s"
            param = [s, service_charge, a]
            update(sql, param)
            m = m - s - service_charge
            # 转入账号加上转入额
            sql = "update ny_bank set money = money  + %s where account = %s"
            param = [s, b]
            update(sql, param)
            print("转账成功，您现在的余额为￥", m)
            return 1
        else:
            return 3  # 余额不足
    else:
        return 2  # 账号不存在


# 存钱操作
def save():
    a = sign_in()  # 登录
    if a == 2 or a == 1:
        return a
    else:
        s = int(input("请输入您要储存的金额:"))
        # 在数据库修改金额
        sql = "update bank set money = money  + %s where account = %s"
        param = [s, a]
        update(sql, param)
        # 在数据库查询金额
        sql = "select money from bank where account = %s"
        param = [a]
        m = select(sql, param)
        for i in m:
            m = i[0]
        print("储存成功，您现在的余额为￥", m)


# 取钱操作
def withdraw():
    a = sign_in()
    if a == 2 or a == 1:
        return a
    else:
        s = int(input("请输入您要取出的金额:"))
        # 在数据库查询金额
        sql = "select money from bank where account = %s"
        param = [a]
        m = select(sql, param)
        for i in m:
            m = i[0]
        if s <= m:  # 余额判断
            # 在数据库修改金额
            sql = "update bank set money = money  - %s where account = %s"
            param = [s, a]
            update(sql, param)
            m -= s
            print("取出成功，您现在的余额为￥", m)
        else:
            print("你没那么多钱，爬")


# 转账操作
def transfer():
    a = sign_in()
    if a == 2 or a == 1:
        return a
    else:
        b = input("请输入你要转账的账号:")
        # 在数据库查询转账账号
        sql = "select account from bank"
        u1 = select(sql)
        data = []
        for i in u1:  # 遍历所有账号
            data.append(i[0])
        u1 = data  # 账号表
        if b in u1:  # 本行转账
            s = int(input("请输入转出的金额:"))
            # 在数据库查询金额
            sql = "select money from bank where account = %s"
            param = [a]
            m = select(sql, param)
            for i in m:
                m = i[0]
            if s <= m:
                # 转出账号减去转出额
                sql = "update bank set money = money  - %s where account = %s"
                param = [s, a]
                update(sql, param)
                m -= s
                # 转入账号加上转入额
                sql = "update bank set money = money  + %s where account = %s"
                param = [s, b]
                update(sql, param)
                print("转账成功，您现在的余额为￥", m)
            else:
                print("你没那么多钱，爬")
        else:
            # 本行不存在账户，进入跨行数据库判断
            n = Super_transfer(a, b)
            if n == 1:
                pass
            elif n == 2:
                print("转账账号不存在")
            elif n == 3:
                print("你没那么多钱，爬")


# 查询账户信息操作
def search():
    a = sign_in()
    if a == 2 or a == 1:
        return a
    else:
        print("以下是你的个人信息:")
        sql = "select * from bank where account = %s"
        param = [a]
        u = select(sql, param)
        u = u[0]
        print(u)
        info = '''
                ---------------个人信息----------------
                账号:%s
                密码:%s
                姓名:%s
                地址:%s,%s,%s,%s
                余额:%s
                开户行:%s
            '''
        print(info % (u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8]))


# 用户操作—开户
def bank_addUser(username, password, country, province, street, door):
    account = str(random.randint(10000000, 99999999))  # 随机生成8位数账号
    # 获取账号数据,以判断是否重复
    sql = "select account from bank"
    acc = select(sql)
    data = []
    for i in acc:  # 遍历所有账号
        data.append(i[0])
    acc = data
    while account in acc:
        account = str(random.randint(10000000, 99999999))  # 假如账号重复，重随账号

    # 2.正常开户，将用户信息存在数据库
    sql = "insert  bank  value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, password, username, country, province, street, door, 0, bank_name]
    update(sql, param)
    return account


# 用户操作逻辑
def addUser():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    country = input("请输入国家:")
    province = input("请输入省份:")
    street = input("请输入街道:")
    door = input("请输入门牌号:")
    # 将数据传输给银行
    status = bank_addUser(username, password, country, province, street, door)
    account = status
    print("开户成功，以下是您的个人信息")
    info = '''
        ---------------个人信息----------------
        账号:%s
        密码:%s
        姓名:%s
        地址:%s,%s,%s,%s
        余额:%s
        开户行:%s
    '''
    print(info % (account, username, password, country
                  , province, street, door,
                  0,
                  bank_name))


# 主界面
def welcme():
    print("----------------------------------")
    print("-      中国工商银行账户管理系统       -")
    print("----------------------------------")
    print("-     1.开户                      -")
    print("-     2.存钱                      -")
    print("-     3.取钱                      -")
    print("-     4.转账                      -")
    print("-     5.查询                      -")
    print("-     6.退出                      -")
    print("----------------------------------")


# 主程序
def start():
    while True:
        welcme()
        chose = input("请输入您的业务编号:")
        if chose == '1':
            addUser()
        elif chose == '2':
            save()
        elif chose == '3':
            withdraw()
        elif chose == '4':
            transfer()
        elif chose == '5':
            search()
        elif chose == '6':
            print("欢迎下次光临━(*｀∀´*)ノ亻!")
            exit()
        else:
            print("输入错误，请重新输入")


start()  # 开始运行
