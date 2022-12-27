#usamos esta ventana main.py como prueba para ver si funcionaba uvicorn y fastapi
from typing import Union
from fastapi import FastAPI


from models.item_model import Item


app = FastAPI()


#tipos de parametros de una ruta
@app.get("/")
def read_root():
    return {"Hola": "Mundooo!!!!!!"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
#creando nuevas rutas con parametros
@app.get('/calculadora')
def calcular(operando1:float, operando2:float):
    return {'suma':operando1 + operando2}

@app.put('/items/{item_id}')
def update_item(item_id:int, item: Item):
    return{'item_name': item.name, 'item_id': item_id, 'item_price': item.price}





