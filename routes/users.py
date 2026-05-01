# from bson import ObjectId
from fastapi import APIRouter, HTTPException
from models.users  import User
from config.db import conn
from schemas.users import userEntity, usersEntity
from bson import ObjectId
from bson.errors import InvalidId
user=APIRouter()


@user.get("/users")
async def getAllUser():
   
    print(usersEntity(conn.usersdb.users.find()))
    return usersEntity(conn.usersdb.users.find()) 


@user.get("/users/{id}")
async def get_users(id):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    user = conn.usersdb.users.find_one({"_id": obj_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user["id"] = str(user["_id"])
    print(user)
    return user

@user.post("/users")
async def create_user(user:User):
    # conn.local.insert_one(user)
    # print("user created ==> "+user)
    conn.usersdb.users.insert_one(dict(user))

    return usersEntity(conn.usersdb.users.find()) 


@user.post("/users/{id}")
async def update_user(id,user:User):
    conn.usersdb.users.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})

    return userEntity(conn.usersdb.users.find_one({"_id":ObjectId(id)})) 

@user.post("/users/{id}")
async def delete_user(id):
    conn.usersdb.users.find_one_and_delete({"_id":ObjectId(id)})
    return "user succssFully deleted" 