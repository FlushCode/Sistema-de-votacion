# -*- coding: cp1252 -*-
import validararchivo
directorio = "candidatos.csv"
#Indicar aquí el nombre del archivo#
LISTA_CAMPOS = []
import votacion
VOTOS_TOTALES = {}
MENU_PRINCIPAL = \
["Votar","Ver los resultados","Guardar los resultados","Salir"]
MENU_VOTAR = \
["Lista completa","Por cargo","Volver"]
SEPARADOR = "------------"
def mostrar_menu(menu):
        """Pre: Recibe una lista
        Post: Imprime cada elemento de la lista, asignando a cada
        elemento un numero, comenzando por el 1, luego el 2,
        y así sucesivamente, y la imprime por pantalla
        con un determinado formato
        """
        menu = list(enumerate(menu, start = 1))
        enumeracion = 0
        opciones = 1
        for tupla in menu:
            print str(tupla[enumeracion])+".",tupla[opciones]
def opcion_valida\
    (eleccion,maxeleccion):
    """Pre: Recibe dos numeros, de cualquier tipo,
        Post: Si el primer numero es menor o igual al segundo,
        y mayor que 0, devuelve True, caso contrario None
        Aclaracion: En este programa jamás recibirá numeros negativos
    """
    if eleccion.isdigit():
        if int(eleccion) <= maxeleccion and int(eleccion) > 0:
            return True
def mostrar_resultados\
    (cargos_dic,cantidad_partidos,listas_con_votos,votos_cargos):
    """Pre: Recibe un diccionario cargos_dic
    donde los cargos son las claves, la cantidad de partidos son la
    cantidad de listas en el archivo, listas_con_votos es una lista
    con el formato lista,cargo,nombre,votos y votos_cargos es un
    diccionario con los cargos como claves, y sus valores son los
    votos totales que se halla efectuado para cada cargo
    
    Post: Llama a la funcion mostrar_resultados del módulo votacion
    y los parametros que recibe son los mismos de esta funcion
    """    
    print SEPARADOR
    votacion.mostrar_resultados(cargos_dic,cantidad_partidos,listas_con_votos,votos_cargos)
    print SEPARADOR
    volver = "centinela"
    while volver != "volver":
        volver = raw_input("Ingrese '""volver""' para volver al menu principal: ")
def votaciones\
    (dic_con_cargos,dic_con_partidos,cantidad_partidos,votos_parciales,votos_cargos):
    """Pre: Recibe un diccionario dic_con_cargos
    donde los cargos son las claves, la cantidad de partidos son la
    cantidad de listas en el archivo, votos_parciales es una lista
    con el formato lista,cargo,nombre,votos y votos_cargos es un
    diccionario con los cargos como claves, y sus valores son los
    votos totales que se halla efectuado para cada cargo
    
    Post: Llama a las funciones votar_cargo y votar_lista_completa
    del modulo votacion, y se efectuan las modificaciones en
    votos_parciales y votos_cargos
    """   
    print SEPARADOR
    cantidad_opciones_men_votar = len(MENU_VOTAR)
    votar_lista_completa = 1
    votar_por_cargo = 2
    volver = len(MENU_VOTAR)
    eleccion_votar = 0
    while int(eleccion_votar) != volver:
        mostrar_menu(MENU_VOTAR)
        eleccion_votar = raw_input("Escoja una manera de votar: ")
        if opcion_valida(eleccion_votar,cantidad_opciones_men_votar):
            if int(eleccion_votar) == votar_lista_completa:
                print SEPARADOR
                votacion.votar_lista_completa\
                (dic_con_partidos,cantidad_partidos,votos_parciales,votos_cargos)
            if int(eleccion_votar) == votar_por_cargo:
                print SEPARADOR
                votacion.votar_cargo\
                (dic_con_cargos,cantidad_partidos,votos_parciales,votos_cargos)
            if int(eleccion_votar) == volver:
                break
        else:
            print "vuelva a intentar"
            eleccion_votar = 0

   
def main():
    """Programa para llevar a cabo votaciones"""
    try:
        if validararchivo.formato_correcto(directorio,LISTA_CAMPOS):
            if validararchivo.postulaciones_correctas(LISTA_CAMPOS):
                cargos_dic = validararchivo.cargos_a_diccionario(LISTA_CAMPOS)
                partidos_dic = validararchivo.partidos_a_diccionario(LISTA_CAMPOS)
                listas_con_votos = validararchivo.listas_votar(LISTA_CAMPOS)
        else:
            raise TypeError
        cantidad_partidos = len(partidos_dic)
        votos_ordenados_por_cargo = votacion.votos_por_cargo(VOTOS_TOTALES,cargos_dic)
        cantidad_opciones_men_principal = len(MENU_PRINCIPAL)
        votar = 1
        ver_resultados = 2
        guardar_resultados = 3
        salir = len(MENU_PRINCIPAL)
        eleccion = 0
        while int(eleccion) != salir:
            print SEPARADOR
            mostrar_menu(MENU_PRINCIPAL) 
            eleccion = raw_input("Escoja una opcion: ")
            if opcion_valida(eleccion,cantidad_opciones_men_principal):            
                if int(eleccion) == votar:
                    votaciones\
                (cargos_dic,partidos_dic,cantidad_partidos,\
                 listas_con_votos,votos_ordenados_por_cargo)
                elif int(eleccion) == ver_resultados:
                    mostrar_resultados\
                (cargos_dic,cantidad_partidos,listas_con_votos,\
                 votos_ordenados_por_cargo)
                elif int(eleccion) == guardar_resultados:
                    votacion.exportar_votos(listas_con_votos)
                    print "Los resultados se han guardado con exito"
            else:
                print "Vuelva a intentar"
                eleccion = 0
    except AttributeError:
        print "Se esta presentando nombres de candidatos o partidos con nombre de algun cargo, esto podria confundir al votante y se ha finalizado la ejecucion del programa"
    except TypeError:
        print "El archivo proporcionado no provee ninguna propuesta del tipo lista,cargo,nombre"
    except KeyError:
        print "La cabecera del archivo no coincide con el formato lista,cargo,nombre"
    except ValueError:
        print "Se estan repitiendo cargos, o alguna lista presenta cargos que otra no"
    except IOError:
        print "Formato invalido o archivo inexsistente"
           

main()

    
