# -*- coding: cp1252 -*-


import csv

NOMBRE_PARTIDO = 0
NOMBRE_CARGO = 1
NOMBRE_CANDIDATO = 2
def importar_listas(archivo,lista):
    """Pre: Recibe un archivo CSV con el cabecera
       lista,cargo,nombre y una lista vacia para ser
       modificada
       
       Post: Devuelve una lista de listas, en el cual cada
       lista es de longitud 3 y cada campo representa en el
       mismo orden la cabecera del archivo
    """
    with open(archivo,"rb") as archivo_candidatos:
        archivo_candidatos_csv = csv.DictReader(archivo_candidatos)
        for campos in archivo_candidatos_csv:
            lista+=[[campos["lista"],campos["cargo"],campos["nombre"]]]
    return lista

def formato_correcto(archivo,lista_campos):
    """Pre: Recibe un archivo y una lista vacía.

    Post: Crea una nueva lista, la cual es generada a partir de
    aplicar la funcion importar_listas a los parametros
    recibidos, luego itera sobre la lista para ver que no
    halla ningun campo lista,cargo,nombre sin definir en el
    archivo.
    Aclaracion: Sin definir se refiere a None, no a un espacio
    o un caracter vacio
    """    
    lista = importar_listas(archivo,lista_campos)
    for sublista in lista:
        if None in sublista:
            raise IOError\
            ("Este archivo presenta un formato no valido para el programa")
    return lista

def partidos_a_diccionario(lista):
    """Pre: Recibe una lista de listas.

    Post: Devuelve un diccionario, en el cual los primeros
    elementos de las sublistas son las claves
    (si la clave se repite, se crea otra sublista para los
    nuevos valores que quieren ingresar), y los valores son
    el segundo y tercer elemento de cada sublista.
    """
    diccionario_partidos = {}
    for sublista in lista:
        if sublista[NOMBRE_PARTIDO] in diccionario_partidos:
           diccionario_partidos[sublista[NOMBRE_PARTIDO]]\
            +=[sublista[NOMBRE_CARGO:]]
        else:
           diccionario_partidos[sublista[NOMBRE_PARTIDO]]\
            =[sublista[NOMBRE_CARGO:]]
    return diccionario_partidos
         
def cargos_a_diccionario(lista):
    """Pre: Recibe una lista de listas.

    Post: Devuelve un diccionario, en el cual los segundos
    elementos de las sublistas son las claves
    (si la clave se repite, se crea otra sublista para los
    nuevos valores que quieren ingresar),
    y los valores son el primer y tercer elemento de cada
    sublista.
    """
    diccionario_cargos = {}
    for sublista in lista:
        if sublista[NOMBRE_CARGO] in diccionario_cargos:
            diccionario_cargos[sublista[NOMBRE_CARGO]]\
            +=[[sublista[NOMBRE_PARTIDO],\
                sublista[NOMBRE_CANDIDATO]]]
        else:
            diccionario_cargos[sublista[NOMBRE_CARGO]]\
            =[[sublista[NOMBRE_PARTIDO],\
               sublista[NOMBRE_CANDIDATO]]]
    return diccionario_cargos


def postulaciones_correctas(lista):
    """Pre: Recibe una lista del formato lista,cargo,nombre.

    Post: Itera sobre la lista y si los cargos no se repiten,
    ni hay cargos que no proponga otro partido, ni hay candidatos con
    el nombre de un cargo, devuelve True,
    caso contrario, lanza una excepción.
    Se lanza ValueError si se repiten cargos en una mismo partido o
    si un partido presenta un cargo que otro no.
    Se lanza AttributeError si hay candidatos con nombres de cargos,
    o partidos con nombre de cargos 
    """
    cargos = cargos_a_diccionario(lista).keys()
    listas = partidos_a_diccionario(lista).keys()
    cantidad_listas = len(listas)
    propuestas_por_cargo = partidos_a_diccionario(lista).values()
    posicion_cargo = 0
    posicion_nombre = 1
    cantidad_postulantes_cargo = 1
    #Esta variable la defino asi, ya que la consigna del TP me lo pide
    for cargo in cargos:
        for lista in propuestas_por_cargo:
            coincidencias = 0
            for propuesta in lista:
                if propuesta[posicion_cargo] == cargo:
                    coincidencias+=1
            if coincidencias != cantidad_postulantes_cargo:
                raise ValueError\
            ("Se ha detectado que, el cargo de",cargo,\
             "no se encuentra o se repite mas de una vez en alguna lista")
            
    for lista in propuestas_por_cargo:
        for propuesta in lista:
            if propuesta[posicion_nombre] in cargos\
               or propuesta[posicion_cargo] in listas :
                raise AttributeError
    
    return True


def listas_votar(lista):
    """Pre: Recibe una lista de listas
    Post: Se devuelve una copia de la lista,
    en donde a cada lista se le agrega un 0 entero al final
    """
    listas_votar = [x[:] for x in lista]
    for lista in listas_votar:
        lista.append(0)
    return listas_votar 

