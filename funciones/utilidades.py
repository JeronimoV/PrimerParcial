def parsear_a_numero(numero:str):
    """Parseo de una forma segura a int

    Args:
        numero (str): El numero de formato str que quiero pasar a int

    Returns:
        int: Si la comprobacion dio todo correcto, devuelve el str transformado a int
        bool: Si algo salio mal al tratar de convertirlo, devuelve False
    """    
    for i in range(len(numero)):
        respuesta = numero[i].isnumeric()
        if respuesta == False:
            return False
    return int(numero)


def formatear_texto(lista_texto:list[dict]) -> None:
    """Le da una forma al texto ingresado para printear

    Args:
        lista_texto (list[dict]): Es la lista con la informacion que quiero formatear
    """    
    if len(lista_texto) == 0:
        print("No hubo peliculas encontradas con los datos proporcionados")
    else:
        
        print(""""
*************************************************************************************************************
|   "Titulo"   |    "Genero"    |   "Año de Lanzamiento"    |   "Duracion"  |   "ATP"   |   "Plataformas    | 
-----------------------------------------------------------------------------------------""")
        for i in range(len(lista_texto)):
            plataformas = ""
            for l in range(len(lista_texto[i]["Plataformas"])):
                plataformas = plataformas + f"{lista_texto[i]["Plataformas"][l]}  "
            print(f"|   {lista_texto[i]["Titulo"]}  |   {lista_texto[i]["Genero"]}  |   {lista_texto[i]["Año_de_Lanzamiento"]}  |   {lista_texto[i]["Duracion"]}  |   {lista_texto[i]["ATP"]}  |    {plataformas}     |")


def buscar_peliculas(lista_busqueda:list , clave:str, valor, buscar_varios:bool ) -> dict:
    """Da varias opciones de busqueda de peliculas

    Args:
        lista_busqueda (list[dict]): Es la lista donde quiero buscar la informacion 
        clave (str): Es la Key del valor que quiero usar para encontrar la data
        valor (_type_): Es el valor que debe tener la key que busco
        buscar_varios (bool): Si es True, buscara mas de una coincidencia y las devolvera, sino solo buscara una

    Returns:
        list[dict]: Si buscar_varios es True y todo salio bien, devuelve todas las coincidencias
        dict: Si buscar_varios es False y todo salio bien, devuelve solo una coincidencia
    """    
    lista_peliculas = []
    retorno = None
    for i in range(len(lista_busqueda)):
        dato_busqueda = lista_busqueda[i][f"{clave}"]
        valor_busqueda = valor
        
        if clave == "Titulo": #Esto es asi por si pasan un valor tipo el de "ATP" que es bool, no se rompa
            valor_busqueda = valor.upper()
            dato_busqueda = lista_busqueda[i][f"{clave}"].upper()
        
        if dato_busqueda == valor_busqueda:
            match buscar_varios:
                case True:
                    lista_peliculas.append(lista_busqueda[i])
                case False:
                    retorno = lista_busqueda[i]
    if len(lista_peliculas) > 0:
        retorno = lista_peliculas
    return retorno

def buscar_plataformas(lista_busqueda:list[dict]):
    """Busca plataformas especificadas

    Args:
        lista_busqueda (list[dict]): Es la lista donde quiero buscar la informacion 

    Returns:
        list[dict]: Si todo salio bien y hubo resultados, devuelve una lista con las peliculas que contienen esa plataforma
        None: No hubo coincidencias, asi que no devuelve nada
    """    
    plataforma = input("Escribe la plataforma que quieres buscar: ")
    lista_plataformas = []
    retorno = None
    for i in range(len(lista_busqueda)):
        for l in range(len(lista_busqueda[i]["Plataformas"])):
            if lista_busqueda[i]["Plataformas"][l].upper() == plataforma.upper():
                lista_plataformas.append(lista_busqueda[i])
    if len(lista_plataformas) > 0:
        retorno = lista_plataformas
    return retorno

def ordenar_peliculas_modulo(lista_ordenar:list, clave:str) -> list:
    """Ordena el codigo

    Args:
        lista_ordenar (list): Es la lista donde quiero buscar la informacion 
        clave (str): Es la Key que usare para ordenar por justamente por keys

    Returns:
        list: _description_
    """    
    retorno = None
    orden = input("Lo quieres ordenar de forma ascendente o descendente?")

    while orden != "ascendente" and orden != "descendente":
        orden = input("Error, lo quieres ordenar de forma ascendente o descendente?")

    for i in range(len(lista_ordenar)):
        for l in range(len(lista_ordenar) - i - 1):
            match orden:
                case "descendente":
                    if lista_ordenar[l][f"{clave}"] < lista_ordenar[l + 1][f"{clave}"]:
                        auxiliar = lista_ordenar[l]
                        lista_ordenar[l] = lista_ordenar[l + 1]
                        lista_ordenar[l + 1] = auxiliar
                case "ascendente":
                    if lista_ordenar[l][f"{clave}"] > lista_ordenar[l + 1][f"{clave}"]:
                        auxiliar = lista_ordenar[l]
                        lista_ordenar[l] = lista_ordenar[l + 1]
                        lista_ordenar[l + 1] = auxiliar
                case _:
                    return "Opcion no valida, algo salio mal"
    retorno = lista_ordenar
                
    if type(lista_ordenar[0][f"{clave}"]) == str: #Como en los str, cada letra es representada por un valor, necesito darlo vuelta el resultado para que cumpla las condiciones
        lista_reversa = []
        for i in range(len(lista_ordenar)):
            lista_reversa.append(lista_ordenar[len(lista_ordenar)-i-1])
        retorno = lista_reversa

    return retorno