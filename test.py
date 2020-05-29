import mysql.connector
mydb=mysql.connector.connect(host=,user=,password=,database=,port=)
print("hey i think iam connected")
cur=mydb.cursor()
imaged="tapas.jpg"
cur.execute("insert into testing""(image)""values(%s)",("tapas.jpg",) )
mydb.commit();
mydb.close()