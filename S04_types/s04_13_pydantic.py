from datetime import datetime
from pydantic import BaseModel #clase para modelos que creemos


#crear clase usuario
class Users(BaseModel):
    id:int
    name = 'Francisco Serafini'
    signup_ts: datetime | None = None
    friends: list[int] = []

#podriamos recibir estos datos
external_data = {
    'id': 1001,
    'signup_ts': '2022-12-29 23:53',
    'friends':[1002, 1003, 1004]
}
#creamos un nuevo usuario
user = Users(**external_data)
print(user)
print(user.id)