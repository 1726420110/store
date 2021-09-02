import time

dic = {}
date = []

try:
    while True:
        file = open(file=r"baidu_x_system.log", mode="r+", encoding="utf-8")
        #  w:写   r:读取   a:附加   b:字节
        date = file.readlines()
        for line in date:
            # 已知是空格分隔，那就是分割字符串，用split()函数。这个函数的参数是分隔符，空格是默认值可以不写。返回值是分割后的子串组成的字符串列表。
            ip = line.split(" ")[0]
            if ip in dic:
                dic[ip] += 1

            else:
                dic[ip] = 1
        print(dic)
        time.sleep(60)

except FileNotFoundError:
    print("没有这个文件！重新适配文件！")
finally:
    file.close()  # 关闭资源
