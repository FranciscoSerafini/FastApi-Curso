from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI() #creacion de la instancia 
router = APIRouter()

#iniciamos el servidor: uvicorn users:app --reload
#creacion de la solicitud
#entidad user
class user(BaseModel):
    name:str
    surname:str
    url:str
    age:int


users_list = [  user  ( id=1 ,name="Francisco", surname ="Serafini", url="https://moure.dev", age= 23 ),
                user(id=2 ,name="Francis", surname ="DEV", url="https://Francisco.dev.com", age=23 ),        
                user(id=3 ,name="Fran", surname ="Developer",url= "https://Fran.dev.com.ar", age= 23 )]


@app.get("/usersjson")
async def usersjson():
    return [{"id":"1","name": "Francisco", "surname": "Serafini", "url":"https://moure.dev","age":23 },
            {"id":"2","name": "Francis", "surname": "DEV", "url":"https://Francisco.dev.com","age":23},
            {"id":"3","name": "Fran", "surname": "Developer", "url":"https://Fran.dev.com.ar","age":23 }]

@app.get("/users")
async def users():
    return users_list

#path
@app.get("/user_francisco/{id}") 
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list (users_list)[0]
    except:
        return {'No se encontrado el usuario':'error'}
#query
@app.get("/userquery") 
async def user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list (users_list)[0]
    except:
        return {'No se encontrado el usuario':'error'}
#hora de video 2:06


