persona = {}
continuar = True
while continuar:
    clave = input( '¿Qué dato quieres introducir?' )
    valor = input ('Introduce el ' + clave + ': ')
    persona[clave] = valor
    print (persona)
    respuesta = input ('¿Quieres continuar (S/N)?')
    if respuesta == 'N':
        continuar = False

