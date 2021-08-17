import random

# 准备数据库和开户行名称
users = {
    "30000000":{
        "password":"123456",
        "username": "张三",
        "country": "中国",
        "province": "北京",
        "street": "昌平",
        "door": "5",
        "money":10000,
        "bank_name":"中国农业银行昌平支行"
    },
    "40000000":{
        "password":"123456",
        "username": "李四",
        "country": "中国",
        "province": "北京",
        "street": "昌平",
        "door": "6",
        "money":2000,
        "bank_name":"中国农业银行昌平支行"
    },
}
bank_name = "中国农业银行昌平支行"

def sign_in():
    a = input("请输入您的账号:")
    if a in users :
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



def save():
    a = sign_in()
    if a == 2:
        pass
    else :
        s = int(input("请输入您要储存的金额:"))
        users[a]["money"] = users[a]["money"] + s
        print("储存成功，您现在的余额为￥",users[a]["money"])
        pass



def withdraw():
    a = sign_in()
    if a == 2 or a == 1:
        pass
    else :
        s = int(input("请输入您要取出的金额:"))
        m = users[a]["money"]
        if s <= m:
            users[a]["money"] = users[a]["money"] - s
            print("取出成功，您现在的余额为￥",users[a]["money"])
        else:
            print("你没那么多钱，爬")


def transfer():
    a = sign_in()
    if a == 2 or a == 1:
        pass
    else :
        b = input("请输入你要转账的账号:")
        s = int(input("请输入转出的金额:"))
        users[a]["money"] = users[a]["money"] - s
        users[b]["money"] = users[b]["money"] + s
        print("转账成功，您现在的余额为￥",users[a]["money"])
        pass

def search():
    a = sign_in()
    if a == 2:
        pass
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
        pass

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
