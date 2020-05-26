import MySQLdb


db=MySQLdb.connect('210.119.12.52','test_usr','mysql_p@ssw0rd','shopdb',charset='utf8')
cur = db.cursor()
cur.execute('select * from producttbl')

while True:
    product = cur.fetchone()
    if not product:
        break
    print(product)

cur.close()
db.close()
