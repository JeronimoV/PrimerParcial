from validaciones import *
from funciones.utilidades import *
from manipulacion_archivos import crear_json

def crear_pelicula(lista_peliculas) :
    """_summary_

    Args:
        lista_peliculas (list[dict]): Aca estan todas las peliculas

    Returns:
        None : No devuelve nada, ya que solo crea y carga la pelicula
    """    

    print("Bienvenido a la opcion de creacion de peliculas")

    titulo = validar_titulo(lista_peliculas)
    genero = validar_genero()
    duracion = validar_duracion()
    fecha = validar_fecha()
    atp = validar_atp()
    plataformas = validar_plataformas()

    
    pelicula_anterior = lista_peliculas[len(lista_peliculas)-1]
    id = pelicula_anterior["ID"] + 1

    lista_peliculas.append({
        "ID": id,
        "Titulo" : titulo,
        "Genero" : genero,
        "Duracion" : duracion,
        "Año_de_Lanzamiento" : fecha,
        "ATP" : atp,
        "Plataformas": plataformas
        })
    
    return "Pelicula creada con exito"


def modificar_pelicula(lista_peliculas,titulo:str) -> None:
    """Modifica la informacion de la pelicula que desee el usuario

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 
        titulo (str): EL titulo por el que buscare la pelicula
    """
    lista_de_acciones = []

    pelicula_a_modificar = buscar_peliculas(lista_peliculas, "Titulo", titulo, False)

    if pelicula_a_modificar == None:
        return "Pelicula no encontrada!"
    
    flag = True
    while flag:
        seleccion = input("""Que datos quieres modificar:
                        1) Titulo
                        2) Genero
                        3) Duracion
                        4) Fecha
                        5) ATP
                        6) Plataformas
                        7) Salir
                        """)
        match seleccion:
            case "1":
                nuevo_titulo = validar_titulo(lista_peliculas)
                pelicula_a_modificar["Titulo"] = nuevo_titulo
                print(f"El nombre de la pelicula ahora es {nuevo_titulo}")
                lista_de_acciones.append(f"Modificaste el nombre de una pelicula a {nuevo_titulo}")
            case "2":
                nuevo_genero = validar_genero()
                pelicula_a_modificar["Genero"] = nuevo_genero
                print(f"El genero de la pelicula ahora es {nuevo_genero}")
                lista_de_acciones.append(f"Modificaste el genero de una pelicula a {nuevo_genero}")
            case "3":
                nueva_duracion = validar_duracion()
                pelicula_a_modificar["Duracion"] = nueva_duracion
                print(f"La duracion de la pelicula ahora es {nueva_duracion}")
                lista_de_acciones.append(f"Modificaste la duracion de una pelicula a {nueva_duracion}")
            case "4":
                nueva_fecha = validar_fecha()
                pelicula_a_modificar["Año_de_Lanzamiento"] = nueva_fecha
                print(f"El año de la pelicula ahora es {nueva_fecha}")
                lista_de_acciones.append(f"Modificaste la fecha de una pelicula a {nueva_fecha}")
            case "5":
                atp = validar_atp()
                pelicula_a_modificar["ATP"] = atp
                print(f"Ahora el valor de ATP es: {atp}")
                lista_de_acciones.append(f"Modificaste el ATP de una pelicula a {atp}")
            case "6":
                plataformas = validar_plataformas()
                pelicula_a_modificar["Plataformas"] = plataformas
                print(f"Ahora el valor de plataformas es: {plataformas}")
                lista_de_acciones.append(f"Modificaste las plataformas de una pelicula a {plataformas}")
            case "7":
                break
            case _:
                print("Opcion no valida")

    for i in range(len(lista_de_acciones)):
        print(lista_de_acciones[i])
    return "Ejecucion completada"


def eliminar_pelicula(lista_peliculas,titulo:str) -> str:
    """Elimina la pelicula deseada

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 
        titulo (str): El titulo por el que buscare la pelicula

    Returns:
        str: _description_
    """    
    pelicula_eliminar = buscar_peliculas(lista_peliculas, "Titulo", titulo, False)

    if pelicula_eliminar == None:
        return "Pelicula no encontrada!"
    
    print(f"¿Seguro quieres eliminar la pelicula: {pelicula_eliminar["Titulo"]}")
    respuesta = input("Si/No")

    while respuesta != "Si" and respuesta != "No":
        respuesta = input("Error, responde Si/No")

    if respuesta == "Si":
        lista_peliculas.remove(pelicula_eliminar)
        return "Pelicula eliminada con exito!"
    else:
        return "Operacion Cancelada!"


def mostrar_peliculas(lista_peliculas):
    
    """Muestra las peliculas, teniendo en cuenta la seleccion
    """    
    
    print("""
a. Todas las películas.
b. De determinado género.
c. De determinado año.
d. Todas las ATP
e. Todas las No ATP
f. De determinada plataforma.
""")
    
    seleccion = input("Seleccione una opcion: ")

    match seleccion:
        case "a":
            formatear_texto(lista_peliculas)
        case "b":
            genero_seleccionado = input("De que genero desea buscar?: ")
            valor_encontrado = buscar_peliculas(lista_peliculas, "Genero", genero_seleccionado, True)
            if valor_encontrado == None:
                return "Pelicula/s no encontrada/s!"
            formatear_texto(valor_encontrado)
        case "c":
            año_seleccionado_str = input("De que año desea buscar?: ")
            año_seleccionado = parsear_a_numero(año_seleccionado_str)
            if año_seleccionado != False:
                valor_encontrado = buscar_peliculas(lista_peliculas, "Año_de_Lanzamiento", año_seleccionado, True)
                if valor_encontrado == None:
                    return "Pelicula no encontrada!"
                formatear_texto(valor_encontrado)
        case "d":
            valor_encontrado = buscar_peliculas(lista_peliculas, "ATP", True, True)
            if valor_encontrado == None:
                return "Pelicula no encontrada!"
            formatear_texto(valor_encontrado)
        case "e":
            valor_encontrado = buscar_peliculas(lista_peliculas, "ATP", False, True)
            if valor_encontrado == None:
                return "Pelicula no encontrada!"
            formatear_texto(valor_encontrado)
        case "f":
            valor_encontrado = buscar_plataformas(lista_peliculas)
            if valor_encontrado == None:
                return "Plataforma no encontrada!"
            formatear_texto(valor_encontrado)
        case _:
            print("Opcion no valida")
    return "Operacion finalizada"

def ordenar_peliculas(lista_peliculas):
    """Ordena las peliculas dependiendo de la seleccion

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 
    """    
    
    ultimo_ordenamiento = None

    print("""
a. Título.
b. Género.
c. Año de lanzamiento.
d. Duración.
""")
    seleccion = input("Selecciona una de las opciones:")
    match seleccion:
        case "a":
            nueva_lista = ordenar_peliculas_modulo(lista_peliculas, "Titulo")
            formatear_texto(nueva_lista)
            ultimo_ordenamiento = nueva_lista
        case "b":
            nueva_lista = ordenar_peliculas_modulo(lista_peliculas, "Genero")
            formatear_texto(nueva_lista)
            ultimo_ordenamiento = nueva_lista
        case "c":
            nueva_lista = ordenar_peliculas_modulo(lista_peliculas, "Año_de_Lanzamiento")
            formatear_texto(nueva_lista)
            ultimo_ordenamiento = nueva_lista
        case "d":
            nueva_lista = ordenar_peliculas_modulo(lista_peliculas, "Duracion")
            formatear_texto(nueva_lista)
            ultimo_ordenamiento = nueva_lista
        case _:
            print("Opcion no valida")
    return ultimo_ordenamiento


def buscar_pelicula_titulo(lista_peliculas,Titulo):
    """Busca una pelicula teniendo en cuenta el titulo

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 
        Titulo (str): Es el titulo por el que busca la funcion

    Returns:
        str: Si algo falla, devuelve un texto de error
    """    
    resultado = buscar_peliculas(lista_peliculas, "Titulo", Titulo, False)
    if resultado == None:
        return "Pelicula no encontrada!"
    formatear_texto([resultado])
    return "Ejecucion completada"

def calcular_promedio(lista_peliculas):
    """Calcula el promedio teniendo en cuenta la seleccion

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 
        
    Returns:
        int: Devuelve el resultado de los promedios
    """    
    seleccion = input("""
a. Calcular Promedio de Año de Lanzamiento
b. Calcular Promedio de Duracion de peliculas
""")

    while seleccion != "a" and seleccion != "b":
        print("Opcion no valida")
        seleccion = input("""
a. Calcular Promedio de Año de Lanzamiento
b. Calcular Promedio de Duracion de peliculas
""")
    
    if seleccion == "a":
        seleccion = "Año_de_Lanzamiento"
    else: 
        seleccion = "Duracion"

    contador = 0

    for i in range(len(lista_peliculas)):
        contador += lista_peliculas[i][f"{seleccion}"]

    resultado = contador / (len(lista_peliculas))

    return resultado

def calcular_porcentaje(lista_peliculas):
    """Calcula el procentaje teniendo en cuenta las opciones

    Args:
        lista_peliculas (list[dict]): Es la lista donde quiero buscar la informacion 

    Returns:
        str: texto donde se encuentras los resultados
    """    
    seleccion = input("""
    a. Porcentaje por género.
    b. Porcentaje por ATP.
    """)
        
    while seleccion != "a" and seleccion != "b":
        print("Opcion no valida")
        seleccion = input("""
    a. Porcentaje por género.
    b. Porcentaje por ATP.
    """)
    match seleccion:
        case "a":
            genero_seleccionado = validar_genero()
            contador = 0
            for i in range(len(lista_peliculas)):
                if lista_peliculas[i]["Genero"] == genero_seleccionado:
                    contador += 1
            resultado = (contador*100)/len(lista_peliculas)
            return f"El porcentaje es {resultado}"
        case "b":
            contador_si = 0
            contador_no = 0
            for i in range(len(lista_peliculas)):
                if lista_peliculas[i]["ATP"] == True:
                    contador_si += 1
                else:
                    contador_no += 1
                    
            resultado_si = (contador_si*100)/len(lista_peliculas)
            resultado_no = (contador_no*100)/len(lista_peliculas)
            return f"El porcentaje de Si es : {resultado_si}, el de No es: {resultado_no}"

    #(cantidad_ocupada/100)*cantidad_total
    
def mostrar_por_genero(lista_peliculas):
    generos_vistos = []
    
    lista_resultados = []
    
    #Lista_generos es un tuple creado en el archivo validaciones, la cual contiene todos los generos
    
    for i in range(len(lista_generos)):
        existe_genero = generos_vistos.count(f"{lista_generos[i]}")
        
        if existe_genero < 1:
            resultados = buscar_peliculas(lista_peliculas, "Genero", lista_generos[i],True)
            generos_vistos.append(lista_generos[i])
            if resultados != None:
                lista_resultados.append(resultados)
            
    generos_usados = []
    peliculas_usadas = []
    for i in range(len(lista_resultados)):
        peliculas_genero = []
        mensaje = ""
        genero = ""
        total = 0
        for l in range(len(lista_resultados[i])):
            if mensaje == "":
                mensaje = lista_resultados[i][l]["Genero"] + ": " + lista_resultados[i][l]["Titulo"]
                genero = lista_resultados[i][l]["Genero"]
                generos_usados.append(lista_resultados[i][l]["Genero"])
                peliculas_genero.append(lista_resultados[i][l]["Titulo"])
                total += 1
            else:
                mensaje = mensaje + " ," + lista_resultados[i][l]["Titulo"]
                peliculas_genero.append(lista_resultados[i][l]["Titulo"])
                total += 1
        peliculas_usadas.append(peliculas_genero)
        print(mensaje)
        print(f"Total de peliculas de genero {genero}: {total}")
        total = 0
    crear_json(peliculas_usadas, generos_usados)
    return "Operacion Finalizada"