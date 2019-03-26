#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

palabra = input ('escribe una palabra:')
reversed_word = palabra
palabra= list(palabra)
reversed_word = list(reversed_word)
reversed_word.reverse()
if palabra == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
