from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

if len(argv) < 2:
    print("Please provide a name of a csv file. ex:python importcsv.py myfile.csv")
    exit(1)
else:
    csvfile=argv[1]
    print(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name TEXT, birth DATE, gender CHAR)")
    student = csv.reader(open(csvfile,'r'),delimiter=',',quotechar='"')

    for row in student:
        print('{}'.format(row))
        c.execute("INSERT INTO student(name,birth,gender) VALUES (?,?,?)",(row[0],row[1],row[2]))
        
conn.commit()
conn.close()
exit(0)

