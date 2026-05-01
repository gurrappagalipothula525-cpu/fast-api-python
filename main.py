from fastapi import FastAPI
from routes.userRouter import  user
app =  FastAPI()
app.include_router(user)










# @app.get("/")
# def greet():
#     return("wellcome  to python")
# products=[
#     Product(id=1,name="soap",description="decription one",price=10,quntity=10),
#     Product(id=2,name="watch",description="soap one",price=20,quntity=30),
#     Product(id=3,name="bench",description="bench one",price=50,quntity=20),
#     Product(id=4,name="bottle",description="bottle one",price=60,quntity=190)
    
# ]
# @app.get("/getAllProducts")
# def getAllProducts():
#     return products

# @app.get("/product/{id}")
# def getProduct(id:int):
#     for product in products:
#         if product.id == id:
#             return product
#     return "product not found"



# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://gurrappa:guru1234@cluster0.ofmvxg6.mongodb.net/Project0"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)