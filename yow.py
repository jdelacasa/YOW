"""
    YOW - Your Own Wordlist
    Authors:
        Juan Antonio Velasco Gómez (@juanvelascogomez)
        Antonio Solis Izquierdo (@asolisi)
"""

#Creamos el archivo en el que escribiremos el diccionario
nombre_archivo=input("Introduzca el nombre para su archivo de salida -->  ")
doc=open(nombre_archivo+".txt","w")

#Creamos las listas de palabras que usaremos
lista_palabras=[]
lista_palabras_nueva=[]

#Introducir palabras en la lista para crear el diccionario
palabra=input("Vamos a introducir algunas palabras clave : \n")
while palabra != "salir":
    lista_palabras.append(palabra)
    palabra=input("Introduzca otra palabra: (escribir 'salir' para terminar)\n")

#Imprimos las palabras introducidas
#print(lista_palabras)

for i in lista_palabras:
    for j in lista_palabras:
        if(i!=j):
            lista_palabras_nueva.append(i+j)

#print(lista_palabras_nueva)

#Escribimos la lista de palabras nueva en un archivo de texto
for i in lista_palabras_nueva:
    doc.write(i + "\n")

doc.close()
