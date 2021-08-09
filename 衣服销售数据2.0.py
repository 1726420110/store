print("-----------------欢迎来到艾依莱商城-------------------")

sell1 = 10+69+140+10+60
sell2 = 60+72+35+90+60+60+140
sell3 = 43+25+43+60+43+78
sell4 = 63+24+63+57
sell5 = 63+45+129+63+58+48+63
sell6 = 120
data = {1:["羽绒服",253.6,500,sell1],
        2:["牛仔裤",86.3,600,sell2],
        3:["风衣",96.8,335,sell3],
        4:["皮草",135.9,855,sell4],
        5:["T恤",65.8,632,sell5],
        6:["衬衫",49.3,562,sell6]
        }

print("编号      名称      价格      库存      销量")

for key,value in data.items():
      print('{}'.format(key),
            "      ",'{}'.format(value[0]),
            "    ",'{}'.format(value[1]),
            "    ",'{}'.format(value[2]),
            "    ",'{}'.format(value[3])
            )
print("\t")
sumS = 0
for value in data.values():
      sumS += value[3]

sumM = 0
for value in data.values():
      sumM += float(value[1])*value[3]
print("12月份销售总额为:","%.2f"%sumM)
print("\t")

for value in data.values():
      print("12月每种衣服的销量占比为:",'{}'.format(value[0]),"%.2f%%"%(value[3]/sumS*100))
print("\t")

for value in data.values():
      print("12月每种衣服的销售额占比为:",'{}'.format(value[0]),"%.2f%%"%(value[1]*value[3]/sumM*100))
