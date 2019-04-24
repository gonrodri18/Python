# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def longitud_palabras (text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = text.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def más_repetido(palabras):
    max_palabra = ''
    max_frecuencia= 0
    for palabra, frecuencia in palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(longitud_palabras (texto))
print(más_repetido(longitud_palabras (texto)))