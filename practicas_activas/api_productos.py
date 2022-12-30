from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#creamos un modelo
class producto(BaseModel):
    id:Optional[str]
    nombre:str
    precio_compra:float
    precio_venta:float
    proveedor:str

    
app = FastAPI() 
#creamos una lista de prodcutos
productos = []

@app.get('/') #ruta de bienvenida
def index():
    return{'mensaje':'Bienvenidos a la API de prodcutos'}

@app.get('/producto')
def obtener_productos():
    return productos

@app.post('/prodcuto') #crear datos con post
def crear_producto(producto:producto):
    productos.append(producto)
    return{'mensaje': 'Producto creado satisfactoriamente.'}