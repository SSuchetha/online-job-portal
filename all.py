import mysql.connector,time
import random

def create_connection(host_name, user_name, database):
	connection=None
	try:
		connection=mysql.connector.connect(host=host_name , user=user_name , database=database)
		c=connection.cursor()
	except Error as err:
		print(f"Error: '{err}'")
	return connection,c

def read(mydb,mycursor):
	try:
		res=[]
		mycursor.callproc('getUsers')
		for myresult in mycursor.stored_results():
			res.append(myresult.fetchall())
		return res
	except Exception as e:
		print(e)

def insert(mydb,mycursor,info):

	try:
		sql="select uid from user"
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		while(True):
			new_id=random.randrange(1,100,1)

			if(new_id not in myresult):
				data=[]
				data.append(new_id)
				data.append(info.name)
				data.append(info.dob)
				data.append(info.age)
				data.append(info.skills)
				data.append(info.education)
				data.append(info.contact)
				data.append(info.experience)
				data.append(info.address)
				data.append(info.gender)

				final_data=tuple(data)
				sqlform="Insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				mycursor.execute(sqlform , final_data)
				mydb.commit()
				sql="select current_timestamp()"
				mycursor.execute(sql)
				myresult=mycursor.fetchone()
				res=[]
				res.append(new_id)
				for row in myresult:
					res.append(row)
				return res
			else:
				continue

	except Exception as e:
		print(e)

def update(mydb,mycursor,info,uid):

	try:
		sql="select * from user where uid=%s"
		mycursor.execute(sql,(uid,))
		row=mycursor.fetchall()
		if(row==None):
			return {"Record not found"}

		else:
			if info.name!=None:
				sql="update user set name=%s where uid=%s"
				mycursor.execute(sql,(info.name,uid,))
			if info.dob!=None:
				sql="update user set dob=%s where uid=%s"
				mycursor.execute(sql,(info.dob,uid,))
			if info.age!=None:
				sql="update user set age=%s where uid=%s"
				mycursor.execute(sql,(info.age,uid,))
			if info.skills!=None:
				sql="update user set skills=%s where uid=%s"
				mycursor.execute(sql,(info.skills,uid,))
			if info.education!=None:
				sql="update user set education=%s where uid=%s"
				mycursor.execute(sql,(info.education,uid,))
			if info.contact!=None:
				sql="update user set contact=%s where uid=%s"
				mycursor.execute(sql,(info.contact,uid,))
			if info.experience!=None:
				sql="update user set experience=%s where uid=%s"
				mycursor.execute(sql,(info.experience,uid,))
			if info.address!=None:
				sql="update user set address=%s where uid=%s"
				mycursor.execute(sql,(info.address,uid,))
			if info.gender!=None:
				sql="update user set gender=%s where uid=%s"
				mycursor.execute(sql,(info.gender,uid,))
			mydb.commit()
			return {"Record Updated"}

	except Exception as e:
		print(e)

def delete(mydb,mycursor,uid):
	try:
		check="select * from user where uid=%s"
		mycursor.execute(check,(uid,))
		row=mycursor.fetchone()
		if (row==None):
			return {"Record does not exist"}
		sql="delete from user where uid=%s"
		mycursor.execute(sql,(uid,))
		mydb.commit()
		return {"Record deleted"}
	except Exception as e:
		return e

def readone(mydb,mycursor,uid):
	try:
		sql="select * from user where uid=%s"
		mycursor.execute(sql,(uid,))
		myresult=mycursor.fetchall()
		if(myresult==[]):
			return "Record does not exist"
		return myresult
	except Exception as e:
		print(e)

def get_cost(mydb,mycursor):
	try:
		cost=0
		sql='select * from user'
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		for row in myresult:
			cost=cost+15
		return cost
	except Exception as e:
		print(e)

mydb,mycursor=create_connection('localhost','root','job_portal')
