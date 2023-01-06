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


users_list = [user(name="Francisco", surname ="Serafini", url="https://moure.dev", age= 23 ),
                user(name="Francis", surname ="DEV", url="https://Francisco.dev.com", age=23 ),        
                user(name="Fran", surname ="Developer",url= "https://Fran.dev.com.ar", age= 23 )]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Francisco", "surname": "Serafini", "url":"https://moure.dev","age":23 },
            {"name": "Francis", "surname": "DEV", "url":"https://Francisco.dev.com","age":23},
            {"name": "Fran", "surname": "Developer", "url":"https://Fran.dev.com.ar","age":23 }]

@app.get("/users")
async def users():
    return users_list


#hora de video 2:06


