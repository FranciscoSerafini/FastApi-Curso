#archivo para la creacion de modelos para los items
from pydantic import BaseModel
from typing import Union

#creamos una clase
class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool, None] = None