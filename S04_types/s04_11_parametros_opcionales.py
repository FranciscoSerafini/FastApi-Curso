def say_hi(name:str | None):
    if name is not None:
        print('Hola {name}')
    else:
        print('Hola mundo!')