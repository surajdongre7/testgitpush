import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://suraj7:suraj123@suraj.e1wvp.mongodb.net/?retryWrites=true&w=majority")

import mysql.connector
mydb = client["mydatabase"]
mycol = mydb["customers"]




