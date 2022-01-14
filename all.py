import mysql.connector,time

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
		#print("Reading the database....")
		#time.sleep(1)
		myresult=None
		count=0
		sql="select * from user"
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		#for row in myresult:
		#	print(row)
		return myresult
	except Exception as e:
		print(e)

	print("\n")

def insert(mydb,mycursor,info,uid):
	#print("To insert record...")

	try:
		#id=input("Enter user id ")	
		sql="select * from user where uid=%s"
		mycursor.execute(sql,(uid,))
		myresult=mycursor.fetchone()
		if(myresult==None):	
			"""name=input("Enter name ")
			dob=input("Enter date of birth (YYYY-MM-DD) ")
			age=input("Enter your age ")
			skills=input("Enter skills ")
			education=input("Enter your qualifications ")
			contact=input("Enter phone number nad email id ")
			experience=input("Enter your work experience ")
			address=input("Enter your address ")
			gender=input("Enter gender ")"""

			data=[]
			data.append(uid)
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
			return {"Record inserted"}
			#print('\n')
			#read(mydb,mycursor)
		
		else:
			return {"Record exists"}

	except Exception as e:
		print(e)

def update(mydb,mycursor,info,uid):
	try:
		#id=input("Enter id of the user whose information is to be updated ")
		sql="select * from user where uid=%s"
		mycursor.execute(sql,(uid,))
		row=mycursor.fetchone()
		if(row==None):
			return {"Record not found"}
		else:
			while(1):
				#print("1. Name\n2. DOB\n3. Age\n4. Skills\n5. Education\n6. Contact\n7. Experience\n8. Address\n9. Gender")
				#info=input("Which field do you want to edit ")
				pat=""

				#if(info=='1'):
				#	nn=input("Enter new name ")
					pat="name='{}'".format(info.name)
				#	break
				#elif(info=='2'):
				#	dob=input("Enter correct date of birth ")
					pat="dob='{}'".format(info.dob)
				#	break
				#elif(info=='3'):
				#	age=input("Enter correct age ")
					pat="age='{}'".format(info.age)
				#	break
				#elif(info=='4'):
				#	skills=input("Enter correct skills ")
					pat="skills='{}'".format(info.skills)
				#	break
				#elif(info=='5'):
				#	edu=input("Enter correct education details ")
					pat="education='{}'".format(info.education)
				#	break
				#elif(info=='6'):
				#	contact=input("Enter correct contact ")
					pat="contact='{}'".format(info.contact)
				#	break
				#elif(info=='7'):
				#	ex=input("Enter correct experience ")
					pat="experience='{}'".format(info.experience)
				#	break
				#elif(info=='8'):
				#	add=input("Enter correct address ")
					pat="address='{}'".format(info.address)
				#	break
				#elif(info=='9'):
				#	g=input("Enter correct gender ")
					pat="gender='{}'".format(info.gender)
				#	break
				#else:
				#	print('Enter correct number ')

			if(not pat==''):
				sql="update user set {} where uid={}".format(pat,id)
				mycursor.execute(sql)
				mydb.commit()
				return {"Record Updated"}
	except Exception as e:
		print(e)
	
def delete(mydb,mycursor,uid):
	try:
		#print('Enter the id of the user you want to delete')
		#id=input()
		check="select * from user where uid=%s"
		mycursor.execute(check,(uid,))
		row=mycursor.fetchone()
		if (row==None):
			return {"Record does not exist"}
		sql="delete from user where uid=%s"
		mycursor.execute(sql,(uid,))
		mydb.commit()
		return {"Record deleted"}
		#print('\n')
		#read(mydb,mycursor)
	except Exception as e:
		return e

def readone(mydb,mycursor,uid):
	try:
		#uid=input("Enter user id whose information is to be read ")
		sql="select * from user where uid=%s"
		mycursor.execute(sql,(uid,))
		myresult=mycursor.fetchall()
		if(myresult==[]):
			return "Record does not exist"
		#else:
		#	print(myresult)
		return myresult
	except Exception as e:
		print(e)

mydb,mycursor=create_connection('localhost','root','job_portal')
#read(mydb,mycursor)
#insert(mydb,mycursor)
#update(mydb,mycursor)
#delete(mydb,mycursor)
#readone(mydb,mycursor)
