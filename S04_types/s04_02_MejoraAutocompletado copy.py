def get_full_name(first_name: str, last_name: str, last_name_name :str):
    full_name = first_name.title() + ' ' + last_name.title() + ' ' + last_name_name.title()
    return full_name

print(get_full_name('Fran', 'Serafini', 'Giorgi'))
#print(get_full_name('Fran', 0)) #error de atributo, ya que si le pasariamos un entero el atributo title no puede recibir enteros
