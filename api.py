from fastapi import FastAPI,Path
from pydantic import BaseModel

app=FastAPI()

import mysql.connector
import all

mydb=mysql.connector.connect(user='root' , host='localhost' , database='job_portal')
mycursor=mydb.cursor()

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

@app.post("/insert-data")
def insert_db():
	data=""
	data=all.insert(mydb,mycursor)
	return data

@app.put("/update-db")
def update_db():
	data=""
	data=all.update(mydb,mycursor)
	return data

@app.delete("/delete-one")
def delete_db():
	data=""
	data=all.delete(mydb,mycursor)
	return data
