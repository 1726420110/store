import xlrd

# 打开服装销售数据
Sales_Data = xlrd.open_workbook\
 (filename=r"C:\Users\Administrator\PycharmProjects\pythonProject\Clothing_Sales\2020年每个月的销售情况.xlsx")

Sales_Statistics = {}


month = 1
while month <= 12:  # 12月份 12张表
    Month_Sales = Sales_Data.sheet_by_index(month - 1)  # 每月的表
    rows = Month_Sales.nrows
    for i in range(rows):   # 遍历每月的表
        data = Month_Sales.row_values(i)
        if data[1] == "服装名称":   # 第一行跳过
            pass
        else:
            if data[1] in Sales_Statistics:   # 有则累加
                Sales_Statistics[data[1]]["销售量"] += round(data[4])
                if month in [2, 3, 4]:  # 再次读取的季度判断
                    Sales_Statistics[data[1]]["第"+str(1)+"季"]["销售量"] += round(data[4])
                elif month in [5, 6, 7]:
                    Sales_Statistics[data[1]]["第"+str(2)+"季"]["销售量"] += round(data[4])
                elif month in [8, 9, 10]:
                    Sales_Statistics[data[1]]["第"+str(3)+"季"]["销售量"] += round(data[4])
                elif month in [11, 12, 1]:
                    Sales_Statistics[data[1]]["第"+str(4)+"季"]["销售量"] += round(data[4])

            else:   # 无则新增
                Sales_Statistics[data[1]] = {"销售量": round(data[4]),
                                             "单价": data[2]
                                             }
                # 新建各个季度情况及相关内容定义
                for i in [1, 2, 3, 4]:  # 每种衣服创建4个季度的键值
                    Sales_Statistics[data[1]]["第"+str(i)+"季"] = {"销售量": 0}
                if month in [2, 3, 4]:  # 第一次读取的季度判断
                    Sales_Statistics[data[1]]["第"+str(1)+"季"]["销售量"] = round(data[4])
                elif month in [5, 6, 7]:
                    Sales_Statistics[data[1]]["第"+str(2)+"季"]["销售量"] = round(data[4])
                elif month in [8, 9, 10]:
                    Sales_Statistics[data[1]]["第"+str(3)+"季"]["销售量"] = round(data[4])
                elif month in [11, 12, 1]:
                    Sales_Statistics[data[1]]["第"+str(4)+"季"]["销售量"] = round(data[4])

    month += 1

print(Sales_Statistics)

# 全年销售总额
YM = sum(Sales_Statistics[key]["销售量"] * Sales_Statistics[key]["单价"] for key in Sales_Statistics)   # 计算总销售额YM
YM = round(YM, 2)
print("全年的销售额为:", YM)
# 每件衣服的销售（件数）占比
YS = sum(Sales_Statistics[key]["销售量"] for key in Sales_Statistics)  # 计算总销售量YS
print("每件衣服的销售（件数）占比:")
for key in Sales_Statistics:
    print(key, ":", round(Sales_Statistics[key]["销售量"] / YS * 100, 2), "%")

# 每件衣服的月销售占比  不想算了，把12张月表遍历一下吧

# 每件衣服的销售额占比
print("每件衣服的销售额占比:")
for key in Sales_Statistics:
    print(key, ":", round(Sales_Statistics[key]["销售量"] * Sales_Statistics[key]["单价"] / YM * 100, 2), "%")

# 最畅销的衣服是哪种
print("最畅销的衣服是哪种?")
a = max(Sales_Statistics[key]["销售量"] for key in Sales_Statistics)
for key, value in Sales_Statistics.items():
    if a == Sales_Statistics[key]["销售量"]:
        print(key, a, "件")

# 每个季度最畅销的衣服
print("每个季度最畅销的衣服:")
Season_S = {}   # 每种衣服的季度销售表
for i in [1, 2, 3, 4]:
    Season_S["第"+str(i)+"季"] = {}  # 新建4个季度键值
    for key, value in Sales_Statistics.items():  # 把统计表中的季度销售量数据存储进去
        Season_S["第"+str(i)+"季"][key] = Sales_Statistics[key]["第"+str(i)+"季"]["销售量"]

for i in [1, 2, 3, 4]:  # 找每季度销售量最大值，输出每季度最畅销衣服
    for key, value in Season_S["第"+str(i)+"季"].items():
        if value == max(Season_S["第"+str(i)+"季"].values()):
            print("第"+str(i)+"季:", key, value, "件")


# 全年销量最低的衣服
print("全年销量最低的衣服?")
b = min(Sales_Statistics[key]["销售量"] for key in Sales_Statistics)
for key, value in Sales_Statistics.items():
    if b == Sales_Statistics[key]["销售量"]:
        print(key, b, "件")


