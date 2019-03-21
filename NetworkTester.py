import SpeedCheck
import datetime
import time
import mysql.connector


def check():
	speed = SpeedCheck.Speed_Check()
	print(str(speed) + " speed received.")
	if float(speed) > 0:
		send(speed)

def send(speed):
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'admin',
		passwd = 'raspberry',
		database = 'mydb'
	)

	mycursor = mydb.cursor()

	request = 'INSERT INTO SPEEDS (speed, time) VALUES (%s, %s)'
	val = (str(speed), str(datetime.datetime.now()))
	mycursor.execute(request, val)

	mydb.commit()

while True:
	check()
	time.sleep(10)
