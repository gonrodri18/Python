#Escribir que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud

#opción 1 

def palabras (frase):
    palabras = frase.split()
    longitud = map(len,palabras)
    palabras = dict(zip(palabras,longitud))
    return palabras

frase = input ('Introduce un frase:')
print (palabras(frase))

#opción 2

def palabras (frase):
    return {x:len(x) for x in frase.split()}
frase = input ('intriduce una frase:')
print (palabras(frase))