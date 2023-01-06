from fastapi import FastAPI

app = FastAPI() #creacion de la instancia 

#iniciamos el servidor: uvicorn users:app --reload
#creacion de la solicitud

@app.get("/users")
async def users():
    return "Hola Francisco"

