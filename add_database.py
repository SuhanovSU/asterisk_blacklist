#!/usr/bin/python3

import MySQLdb

#db = MySQLdb.connect(host="rc1c-s8c4zwb4vng2b92n.mdb.yandexcloud.net",  port=3306, user="asterisk", passwd="asterisk",
#                     db="asterisk", ssl={'ca': '~/.mysql/root.crt'})

db = MySQLdb.connect(host="localhost",  port=3306, user="asterisk", passwd="asterisk",
                     db="asterisk")

cursor = db.cursor()
cursor.execute("select * from blacklist")
data = cursor.fetchone()
db.close()
