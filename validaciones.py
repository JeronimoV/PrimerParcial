from funciones.utilidades import *

lista_generos = tuple(["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica", "Comedia dramática",
"Crimen", "Documental", "Drama", "Fantasía", "Histórico", "Infantil", "Musical", "Misterio", "Policíaco", "Romance",
"Ciencia ficción", "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental", "Familiar",
"Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe", "Melodrama", "Erótico", "Cine independiente", 
"Zombies", "Vampiros", "Cyberpunk", "Steampunk", "Distopía", "Utopía", "Road Movie",
"Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"])

def validar_titulo(peliculas:list[dict]) -> str:
    flag = True
    titulo_ingresado = input("Ingrese el titulo de la pelicula, el titulo no debe ser igual al de otra pelicula ni exceder los 30 caracteres: ")
    titulo_len = len(titulo_ingresado)
    

    while flag:
        print(titulo_ingresado)
        print(titulo_ingresado)
        peliculas_encontradas = buscar_peliculas(peliculas, "Titulo", titulo_ingresado, False)
        print("Este es eplis encontradas", peliculas_encontradas)
        if peliculas_encontradas == None :
            flag = False
        else:
            flag = True

        if titulo_len > 30 or flag == True:
            flag = True
            titulo_ingresado = input("Error, ingrese el titulo de la pelicula, el titulo no debe ser igual al de otra pelicula ni exceder los 30 caracteres: ")
            titulo_len = len(titulo_ingresado)
            
    return titulo_ingresado
        


def validar_genero() -> str:
    flag = True
    print("Escribe el genero de tu pelicula, aqui las opciones:")
    for i in range(len(lista_generos)): #Muestra los generos 1 por uno
        print(lista_generos[i])
    genero = input("Escribe aqui: ")
    while flag:
        busqueda_genero = lista_generos.count(genero)
        if busqueda_genero > 0:
            flag = False
        else:
            genero = input("Error, escribe el genero nuevamente: ")
    return genero

def validar_duracion() -> int:
    duracion_str = input("Ingrese la duracion en numeros enteros:")
    duracion = parsear_a_numero(duracion_str)

    while duracion == False or duracion < 1:
        duracion_str = input("Error, ingrese la duracion en numeros enteros:")
        duracion = parsear_a_numero(duracion_str)
    return duracion

def validar_fecha() -> int:
    año_de_lanzamiento_str = input("Ingrese la fecha de lanzamiento de la pelicula, esta debe estar entre 1888 y 2024")
    año_de_lanzamiento = parsear_a_numero(año_de_lanzamiento_str)

    while año_de_lanzamiento == False or año_de_lanzamiento < 1888 or año_de_lanzamiento > 2024:
        año_de_lanzamiento_str = input("Error, ingrese la fecha de lanzamiento de la pelicula, esta debe estar entre 1888 y 2024")
        año_de_lanzamiento = parsear_a_numero(año_de_lanzamiento_str)

    return año_de_lanzamiento

def validar_atp() -> bool:
    atp_respuesta = input("Es apta para todo publico? Si/No")
    atp = None

    while atp_respuesta != "Si" and atp_respuesta != "No":
        atp_respuesta = input("Error, es apta para todo publico? Si/No")

    if atp_respuesta == "Si":
        atp = True
    else:
        atp = False

    return atp

def validar_plataformas():
    
    flag = True
    
    plataformas = []
    
    
    while flag:
        nombre_ingresado = None
        while nombre_ingresado == None or len(nombre_ingresado) > 20 or verificado == False:
            nombre_ingresado = input("Ingrese una plataforma, esta no debe tener numeros y no debe exceder los 20 caracteres:")
            verificado = True
                
            for i in range(len(nombre_ingresado)):
                es_numero = nombre_ingresado[i].isnumeric()
                if es_numero == True:
                    verificado = False
            
        plataformas.append(nombre_ingresado)
        
        seguir = input("Quieres agregar mas plataformas? Si/No")
        
        while seguir != "Si" and seguir != "No":
            seguir = input("Quieres agregar mas plataformas? Si/No")
            
        if seguir == "No":
            flag = False
    
    return plataformas
