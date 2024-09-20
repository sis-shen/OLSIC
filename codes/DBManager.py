import pymysql


stockDB = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='supdriver',
    password='',
    db='stock',
    charset='utf8',
    autocommit=True
)


def sendData(items):
    stockDB.ping(reconnect=True)
    cursor = stockDB.cursor()
    print("开始向数据库插入数据")
    for item in items:
        sql=(f"insert into MaoTai values ({item[0]},"
             f"{item[1]},"
             f"{item[2]},"
             f"{item[3]},"
             f"{item[4]},"
             f"{item[5]},"
             f"{item[6]},"
             f"{item[7]},"
             f"{item[8]},"
             f"{item[9]});")
        # print(sql)
        cursor.execute(sql)
        # print(cursor.fetchall())
    print(f"插入数据成功，总计{len(items)}")

def getAllData(stockDB):
    stockDB.ping(reconnect=True)
    cursor = stockDB.cursor()
    sql= "select * from MaoTai"
    cursor.execute(sql)
    return cursor.fetchall()

def getLatestData():
    stockDB.ping(reconnect=True)

    cursor=stockDB.cursor()
    sql="select * from MaoTai order by timesamp desc"
    cursor.execute(sql)
    alldata = cursor.fetchall()
    resList = []
    for line in alldata:
        resList.append(line)

    return resList
def closeDB():
    stockDB.close()

def clearDB():
    stockDB.ping(reconnect=True)

    cursor = stockDB.cursor()
    sql='delete from MaoTai'
    print("开始清理数据库")
    cursor.execute(sql)
    print('清理完成')