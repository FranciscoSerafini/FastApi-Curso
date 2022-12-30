from typing import Optional
#importamos Optional
def say_hi ( name: Optional [str] = None ):
   if name is not None:
        print('Hola {name}')
   else:
        print('Hola mundo!')
