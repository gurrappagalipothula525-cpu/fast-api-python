from fastapi import APIRouter
from models.user  import User
from config.db import conn
from schemas.usersSchema import userEntity, usersEntity

user=APIRouter()

@user.get("/")
async def getAllUser():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find()) 


@user.post("/")
async def createUser(user:User):
    conn.local.insert_one(user)
    return usersEntity(conn.local.user.find()) 
