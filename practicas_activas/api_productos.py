#modulos incorporados
from uuid import uuid4 as uuid #genera id para productos
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
 

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


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
#get = obtencion de datos
@app.get('/producto')
def obtener_productos():
    return productos
#post = creacion de datos 
@app.post('/prodcuto') #crear datos con post
def crear_producto(producto:producto):
    producto.id = str(uuid())
    productos.append(producto)
    return{'mensaje': 'Producto creado satisfactoriamente.'}

@app.get('/producto/{producto_id}')
def obtener_producto_porId(producto_id:str):
    resultado = list( filter(lambda p: p.id == producto_id, productos))
   
    if len(resultado):
        return resultado[0]
    
    #generamos una exception si no se encuentra el producto

    
    raise HTTPException(status_code= 404, detail= f'El producto con el ID {producto_id} no fue encontrado')

