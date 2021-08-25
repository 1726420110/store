import random


def GTN (m):
    a = random.randint(0, 500)
    while m >= 500:
        bet = input("输入你猜的数字:")
        bet = int(bet)
        if bet < a:
            m = m - 500
            print("小了,现在您的余额为",m)
        elif bet > a:
            m = m - 500
            print("大了,现在您的余额为",m)
        elif bet == a:
            m = m + 10000
            print("恭喜猜中，现在您的余额为",m)
            chose = input("是否继续?y or n:")
            if chose == 'y':
                GTN(m)
            if chose == 'n':
                exit()
        else:
            print("输入有误")
    print("欢迎下次光临")





print("欢迎来到猜数字小游戏,猜测范围0~500")
money = 5000
GTN(money)