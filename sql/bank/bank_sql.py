import pymysql

host = "localhost"
username = "root"
password = ""
database = "company"


def update(sql, param):
    con = pymysql.connect(host=host, user=username, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()


def select(sql, param=None, mode="all", size=0):
    con = pymysql.connect(host=host, user=username, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if mode == "one":
        return cursor.fetchone()
    elif mode == "all":
        return cursor.fetchall()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()
