import random

# 准备数据库和开户行名称
users = {
    "10000000": {
        "password":"123456",
        "username": "张三",
        "country": "中国",
        "province": "北京",
        "street": "昌平",
        "door": "5",
        "money":10000,
        "bank_name":"中国工商银行昌平支行"
    },
    "20000000": {
        "password":"123456",
        "username": "李四",
        "country": "中国",
        "province": "北京",
        "street": "昌平",
        "door": "6",
        "money":2000,
        "bank_name":"中国工商银行昌平支行"
    },
}
bank_name = "中国工商银行昌平支行"

# 登录操作
def sign_in():
    a = input("请输入您的账号:")
    if a in users:
        b = input("请输入您的密码:")
        if b == users[a]["password"]:
            print("登录成功")
            return a
        else:
            print("您的密码错误")
            return 2
    else:
        print("您的账号不存在")
        return 1

# 跨行转账操作
def Super_transfer(a,b):
    from 农业银行 import users1  # 导入农行数据库
    if b in users1:
        s = int(input("请输入转出的金额:"))
        m = users[a]["money"]
        Service_Charge = 0
        if s <= 2000:   # 手续费计算
            Service_Charge = 1.6
        elif 2000 < s <= 5000:
            Service_Charge = 4
        elif 5000 < s <= 10000:
            Service_Charge = 8
        elif 10000 < s <= 50000:
            Service_Charge = 12
        elif s > 50000:
            Service_Charge = round(s*0.0003,2)
            if Service_Charge > 50:
                Service_Charge = 50
        if s <= m + Service_Charge:  # 账款计算
            users[a]["money"] = users[a]["money"] - s - Service_Charge
            users1[b]["money"] = users1[b]["money"] + s
            return 1
        else:
            return 3    #余额不足
    else:
        return 2    #账号不存在

# 存钱操作
def save():
    a = sign_in()   #登录
    if a == 2 or a == 1:
        return a
    else :
        s = int(input("请输入您要储存的金额:"))
        users[a]["money"] = users[a]["money"] + s
        print("储存成功，您现在的余额为￥",users[a]["money"])

# 取钱操作
def withdraw():
    a = sign_in()
    if a == 2 or a == 1:
        return a
    else :
        s = int(input("请输入您要取出的金额:"))
        m = users[a]["money"]
        if s <= m:  #余额判断
            users[a]["money"] = users[a]["money"] - s
            print("取出成功，您现在的余额为￥",users[a]["money"])
        else:
            print("你没那么多钱，爬")

# 转账操作
def transfer():
    a = sign_in()
    if a == 2 or a == 1:
        return a
    else:
        b = input("请输入你要转账的账号:")
        if b in users:  # 本行转账
            s = int(input("请输入转出的金额:"))
            m = users[a]["money"]
            if s <= m:
                users[a]["money"] = users[a]["money"] - s
                users[b]["money"] = users[b]["money"] + s
                print("转账成功，您现在的余额为￥",users[a]["money"])
            else:
                print("你没那么多钱，爬")
        else:   # 本行不存在账户，进入跨行数据库判断
            from 农业银行 import users1  # 导入农行数据库
            n = Super_transfer(a,b)
            if n == 1:
                print("转账成功，您现在的余额为￥", users[a]["money"])
                print(users1[b]["money"])
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
        u = [users[a][x]for x in users[a]]
        info = '''
                ---------------个人信息----------------
                账号:%s
                密码:%s
                姓名:%s
                地址:%s,%s,%s,%s
                余额:%s
                开户行:%s
            '''
        print(info %(a, u[0], u[1], u[2]
                      , u[3], u[4], u[5],
                      u[6], u[7]))

#用户操作—开户
def bank_addUser(account,username,password,country,province,street,door):
    # 1.看银行账户是否已满，满了返回3
    if len(users) > 100:
        return 3

    # 2.正常开户，将用户信息存在数据库
    users[account] = {
        "password":password,
        "username": username,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    return 1

#用户操作逻辑
def addUser():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    country = input("请输入国家:")
    province = input("请输入省份:")
    street = input("请输入街道:")
    door = input("请输入门牌号:")
    account = str(random.randint(10000000,99999999)) #随机生成8位数账号
    while account in users.keys():
        account = str(random.randint(10000000,99999999)) #假如账号重复，重随
    #将数据传输给银行
    status = bank_addUser(account,username,password,country,province,street,door)

    if status == 1:
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
        print(info %(account,username,password,country
                     ,province,street,door,
                     users[account]["money"],
                     bank_name))

    elif status == 3:
        print("对不起，数据库已满")

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


if __name__=="__main__":
    start() #开始运行