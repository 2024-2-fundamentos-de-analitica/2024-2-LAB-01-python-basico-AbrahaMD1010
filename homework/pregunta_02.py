"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""
import csv

def pregunta_02():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Añade los valores de la columna 2 y los convierte en enteros
            # Si existe
            if fila[0] in dic:
                dic[fila[0]] += 1
            # Si no existe
            else:
                dic[fila[0]] = 1

    # Se obtienen los objetos del dic, y se ordenan en base a su letra
    lista = list(dic.items())
    lista.sort()

    return lista

print(pregunta_02())