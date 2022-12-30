from fastapi import FastAPI

app = FastAPI() 
@app.get('/') #ruta de bienvenida
def index():
    return{'mensaje':'Bienvenidos a la API de prodcutos'}