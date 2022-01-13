from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

import mysql.connector
import all

mydb=mysql.connector.connect(user='root' , host='localhost' , database='job_portal')
mycursor=mydb.cursor()

@app.get("/")
def welcome():
	return {"Welcome!!"}

@app.get("/read-db-one")
def read_one():
	data=""
	data=all.readone(mydb,mycursor)
	return data

@app.get("/read-db")
def read_all():
	data=[]
	data=all.read(mydb,mycursor)
	return data

class details(BaseModel):
	uid:int
	name:str
	dob:str
	age:str
	skills:str
	education:str
	contact:str
	experience:str
	address:str
	gender:str

