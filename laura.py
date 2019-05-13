#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extencion .py
#uso de numeros aleatorios

#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)  #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)         #imprimimos el numero generado

#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes,y elegir
#a uno de los participantes aleatoriamente , y retornar esa persona elegida
#Desafio: no volver a retornar una persona ya sorteada

#solucion
#importamos la funcion randint de libreria random
from random import randint
aleatorio=randint(0,80)
print()aleatorio

lista_partici=["ana","jaz","maria"] 
def sorteo_remera(lista_cool):   #definimos una funcion
    #utilizamos len() para saber la cantidad de persona que hay 
    aleatorio=randint(0,2)
    return(lista_partici[aleatorio])

sorteo_remera(lista_partici)


lista_ganador=[] 
lista_partici=["silvi","david","chuaca"]
lista_ganador.append(lista_partici)
