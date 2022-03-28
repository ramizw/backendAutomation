import mysql.connector

# Parameters for connection with mysql
# host, database, user, password
conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
                               user='root', password='root')
print(conn.is_connected())
cursor = conn.cursor()  # Establish a stream between python and database
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
allRecord = cursor.fetchall()
print(allRecord)
sum = 0
for row in allRecord:  # ('selenium', datetime.date(2022, 3, 18), 120, 'Africa')
    sum = sum + row[2]
print(sum)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ('GH', 'Jmeter')
cursor.execute(query, data)

addDetails = 'INSERT INTO CustomerInfo values("WebServices",CURRENT_DATE(),21,"Asia")'
cursor.execute(addDetails)

delQuery = "delete from customerInfo where courseName = 'WebServices'"
# data1 = ('customerInfo', 'WebServices')
cursor.execute(delQuery)
conn.commit()  # Commit in Database

conn.close()
