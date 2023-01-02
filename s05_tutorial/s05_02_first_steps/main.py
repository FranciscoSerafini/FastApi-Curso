from fastapi import FastAPI


app = FastAPI()

@app.get('/') #ruta de inicio
async def index():
    return{'Mensaje': 'Acceso satisfactorio'}