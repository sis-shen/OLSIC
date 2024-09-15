import pymysql


stockDB = pymysql.Connect(
    host='47.99.48.121',
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

    print("Data sended")

def getAllData(stockDB):
    stockDB.ping(reconnect=True)
    cursor = stockDB.cursor()
    sql= "select * from MaoTai"
    cursor.execute(sql)
    return cursor.fetchall()

def getLatestData():
    stockDB.ping(reconnect=True)

    cursor=stockDB.cursor()
    sql="select * from MaoTai order by timesamp desc limit 30"
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
    cursor.execute(sql)
    print('data cleared')