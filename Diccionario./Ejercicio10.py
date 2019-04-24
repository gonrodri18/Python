# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 
# En función de la opción elegida el programa tendrá que hacer lo siguiente:

#1- Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2- Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3- Preguntar por el NIF del cliente y mostrar sus datos.
#4- Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5- Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6- Terminar el programa.


clientes = {}
opción = ''
while opción != '6':
    if opción == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        dirección = input('Introduce la dirección del cliente: ')
        teléfono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':dirección, 'teléfono':teléfono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opción== '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opción == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for key, valor in clientes[nif].items():
                print(key.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opción == '4':
        print('Lista de clientes')
        for key, valor in clientes.items():
            print(key, valor['nombre'])
    if opción == '5':
        print('Lista de clientes preferentes')
        for key, valor in clientes.items():
            if valor['preferente']:
                print(key, valor['nombre'])
    opción = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')