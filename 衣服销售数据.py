print("-----------------欢迎来到艾依莱商城-------------------")
pay1 = 253.6
pay2 = 86.3
pay3 = 96.8
pay4 = 135.9
pay5 = 65.8
pay6 = 49.3
sell1 = 10+69+140+10+60
sell2 = 60+72+35+90+60+60+140
sell3 = 43+25+43+60+43+78
sell4 = 63+24+63+57
sell5 = 63+45+129+63+58+48+63
sell6 = 120

print("编号       名称      价格      库存      销量")
print("1        羽绒服\t  ",pay1,"  500\t\t",sell1)
print("2        牛仔裤\t  ",pay2,"    600\t\t",sell2)
print("3        风衣  \t  ",pay3,"    335\t\t",sell3)
print("4        皮草  \t  ",pay4,"  855\t\t",sell4)
print("5        T恤  \t  ",pay5,"    632\t\t",sell5)
print("6        衬衫  \t  ",pay6,"    562\t\t",sell6)
sumS = sell6+sell5+sell4+sell3+sell2+sell1
sumM = pay1*sell1+pay2*sell2+pay3*sell3+pay4*sell4+pay5*sell5+pay6*sell6
typeS1 = sell1/sumS
typeS2 = sell2/sumS
typeS3 = sell3/sumS
typeS4 = sell4/sumS
typeS5 = sell5/sumS
typeS6 = sell6/sumS
typeM1 = pay1*sell1/sumM
typeM2 = pay2*sell2/sumM
typeM3 = pay3*sell3/sumM
typeM4 = pay4*sell4/sumM
typeM5 = pay5*sell5/sumM
typeM6 = pay6*sell6/sumM
print("12月销售总额为￥","%.2f"%(sumM))
print("每件衣服的销售量占比:")
print("羽绒服","%.2f%%" % (typeS1 * 100),
      "\t牛仔裤","%.2f%%" % (typeS2 * 100),
      "\t风衣","%.2f%%" % (typeS3 * 100),
      "\t皮草","%.2f%%" % (typeS4 * 100),
      "\tT恤","%.2f%%" % (typeS5 * 100),
      "\t衬衫","%.2f%%" % (typeS6 * 100))
print("每件衣服销售额占比:")
print("羽绒服","%.2f%%" % (typeM1 * 100),
      "\t牛仔裤","%.2f%%" % (typeM2 * 100),
      "\t风衣","%.2f%%" % (typeM3 * 100),
      "\t皮草","%.2f%%" % (typeM4 * 100),
      "\tT恤","%.2f%%" % (typeM5 * 100),
      "\t衬衫","%.2f%%" % (typeM6 * 100))

