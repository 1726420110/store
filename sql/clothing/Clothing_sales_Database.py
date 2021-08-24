import xlrd
from clothing_sql import update

# 打开服装销售数据
Sales_Data = xlrd.open_workbook \
    (filename=r"C:\Users\Administrator\PycharmProjects\pythonProject\Clothing_Sales\2020年每个月的销售情况.xlsx")

month = 1
while month <= 12:  # 12月份 12张表
    Month_Sales = Sales_Data.sheet_by_index(month - 1)  # 每月的表
    sql = '''create table mouth_%s (
  `date` VARCHAR(11) NOT NULL,
  `cname` VARCHAR(20) DEFAULT NULL,
  `price` FLOAT(10) DEFAULT NULL,
  `stock` INT(10) DEFAULT NULL,
  `sales` INT(10) DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;'''
    param = [month]
    update(sql, param)
    rows = Month_Sales.nrows
    for i in range(rows):  # 遍历每月的表
        data = Month_Sales.row_values(i)
        if data[1] == "服装名称":  # 第一行跳过
            pass
        else:
            sql = "insert into mouth_%s values (%s,%s,%s,%s,%s)"
            param = [month, data[0], data[1], data[2], data[3], data[4]]
            update(sql, param)

    month += 1
