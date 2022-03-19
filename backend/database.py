from xml.dom.minidom import Document
from model import Todo
#mongodb driver
import motor.motor_asyncio

# mongodb - password = RwY6gX1aK5G7ogGA
'''

client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.rlvdi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

'''
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:RwY6gX1aK5G7ogGA@cluster0.rlvdi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))

    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title,desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}})
    document = await collection.find_one({"title":title})

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True


