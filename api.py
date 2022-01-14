from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional 

app=FastAPI()

import mysql.connector
import all

mydb=mysql.connector.connect(user='root' , host='localhost' , database='job_portal')
mycursor=mydb.cursor()

class details(BaseModel):
	name:str
	dob:str
	age:str
	skills:str
	education:str
	contact:str
	experience:str
	address:str
	gender:str

class updateDetails(BaseModel):
	name : Optional[str]=None
	dob : Optional[str]=None
	age : Optional[str]=None
	skills : Optional[str]=None
	education : Optional[str]=None
	contact : Optional[str]=None
	experience : Optional[str]=None
	address : Optional[str]=None
	gender : Optional[str]=None

@app.get("/")
def welcome():
	return {"Welcome!!"}

@app.get("/read-db-one/{uid}")
def read_one(uid: int=Path(None , description="ID", gt=0)):												
	data=""
	data=all.readone(mydb,mycursor,uid)
	return data

@app.get("/read-db")
def read_all():
	data=[]
	data=all.read(mydb,mycursor)
	return data

@app.post("/insert-data/{uid}")
def insert_db(uid: int , info:details):
	data=""
	data=all.insert(mydb,mycursor,info,uid)
	return data

@app.put("/update-db/{uid}")
def update_db(uid: int , info:updateDetails):
	data=""
	data=all.update(mydb,mycursor,info)
	return data

@app.delete("/delete-one/{uid}")
def delete_db(uid: int=Path(None , description="ID", gt=0)):
	data=""
	data=all.delete(mydb,mycursor,info,uid)
	return data
