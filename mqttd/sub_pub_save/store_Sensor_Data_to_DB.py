#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import datetime
import json
import sqlite3

# SQLite DB Name
DB_Name =  "IoT.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def DHT22_Temp_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	#SensorID = json_Dict['sensor_ID']
	SensorID = "1"
	#Data_and_Time = json_Dict['date']
	Data_and_Time = datetime.datetime.now()	
	Temperature = json_Dict['temperature']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into DHT22_Temperature_Data (SensorID, Date_n_Time, Temperature) values (?,?,?)",[SensorID, Data_and_Time, Temperature])
	del dbObj
	print "Inserted Temperature Data into Database."
	print ""

# Function to save Humidity to DB Table
def DHT22_Humidity_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	#SensorID = json_Dict['sensor_ID']
	SensorID = "2"
	#Data_and_Time = json_Dict['date']
	Data_and_Time = datetime.datetime.now()
	Humidity = json_Dict['humidity']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into DHT22_Humidity_Data (SensorID, Date_n_Time, Humidity) values (?,?,?)",[SensorID, Data_and_Time, Humidity])
	del dbObj
	print "Inserted Humidity Data into Database."
	print ""


#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "dht11/temperature":
		DHT22_Temp_Data_Handler(jsonData)
	elif Topic == "dht11/humidity":
		DHT22_Humidity_Data_Handler(jsonData)	

#===============================================================
