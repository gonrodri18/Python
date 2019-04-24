#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def estadistica(muestra):
    """
    Función que calcula la media, varianza y desviación típica de una muestra.
    parámetros:
       - muestra: Es una lista de números.
    Devuelve:
       - Un diciionario con la media, varianza y desviación típica.
    """
    estadisticas = {}
    media = sum(muestra) / len(muestra)
    estadisticas['media'] =  media
    sum_cuadrados = 0
    for i in muestra:
        sum_cuadrados += i ** 2
    varianza = sum_cuadrados / len (muestra) - media ** 2
    estadisticas['varianza'] = varianza
    estadisticas['desviación típica'] = varianza ** 0.5
    return estadisticas

print (estadistica([1, 2, 3, 4, 5]))

