from threading import Thread
import time

bread = 0


class Cook(Thread):
    __name = ""

    def setName(self, name):
        self.__name = name

    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                bread += 1
                print(self.__name + "做了一个面包，现在有" + str(bread) + "个面包\n", end='')
            else:
                time.sleep(2)


class Eat(Thread):
    __name = ""

    def setName(self, name):
        self.__name = name

    def run(self) -> None:
        global bread
        money = 3000
        eat = 0
        while True:
            if money >= 2.5 and bread > 0:
                money -= 2.5
                bread -= 1
                eat += 1
                print(self.__name + "吃了一个面包，现在有"+str(bread)+"个面包，他还有￥"+str(money)+"\n", end='')
            elif money < 2.5:
                print(self.__name + "吃了" + str(eat) + "个面包\n",end='')
                break
            else:
                time.sleep(3)


c1 = Cook()
c1.setName("1号")
c2 = Cook()
c2.setName("2号")
c3 = Cook()
c3.setName("3号")
e1 = Eat()
e1.setName("一号")
e2 = Eat()
e2.setName("二号")
e3 = Eat()
e3.setName("三号")
e4 = Eat()
e4.setName("四号")
e5 = Eat()
e5.setName("五号")
c1.start()
c2.start()
c3.start()
e1.start()
e2.start()
e3.start()
e4.start()
e5.start()
