def cargar_peliculas():
    """Carga las peliculas desde el csv

    Returns:
        list[dict]: devuelve una lista de diccionarios con la informacion de cada pelicula
    """    
    archivo = open("peliculas.csv", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    
    lineas.pop(0)
    
    lista_peliculas = []
    titulos_vistos = [] #Aqui se almacenan los titulos de las peliculas ya ingresados

    for i in range(len(lineas)): #Aca resto uno para no tomar en cuenta la primera linea
        datos = lineas[i].split(",") #Aca me salteo la primera linea
        id = int(datos[0])
        titulo = datos[1]
        genero = datos[2]
        fecha = int(datos[3])
        duracion = int(datos[4])
        atp_modificar = datos[5]
        atp = None
        
        busqueda = titulos_vistos.count(titulo) #Busco coincidencias para evitar copias
        
        if busqueda == 0:
            titulos_vistos.append(titulo)
            
            if atp_modificar == "Si":
                atp = True
            elif atp_modificar == "No":
                atp = False
            else:
                atp = bool(atp_modificar == "True")
                
            plataformas_modificar = datos[6].split("-")
            plataformas = []
            
            for l in range(len(plataformas_modificar)):
                if len(plataformas_modificar) - 1 == l:
                    plataformas.append(plataformas_modificar[len(plataformas_modificar)-1].replace("\n", ""))
                else:
                    plataformas.append(plataformas_modificar[l])
                    
            lista_peliculas.append({
                "ID": id,
                "Titulo": titulo, 
                "Genero": genero, 
                "Año_de_Lanzamiento": fecha, 
                "Duracion": duracion, 
                "ATP": atp, 
                "Plataformas": plataformas})
    
    return lista_peliculas
        
def guardar_peliculas(lista_peliculas):
    """Guarda las peliculas en el csv

    Args:
        lista_peliculas (list[dict]): Es la lista que almaceno en el csv
    """    
    archivo = open("peliculas.csv", "w", encoding="utf-8")
    archivo.write("ID,Título,Género,Año de lanzamiento,Duración,ATP,Plataformas\n") #Escribo primero esto para que haga de encabezado
    
    for i in range(len(lista_peliculas)):
        posicion = lista_peliculas[i]
        plataformas = None
        for l in range(len(posicion["Plataformas"])):
            if plataformas == None:
                plataformas = posicion["Plataformas"][l]
            else:
                plataformas = plataformas + "-" + posicion["Plataformas"][l]
                
                
        plataformas = plataformas + "\n"
        
        print(plataformas)
        
        formato_guardar = f"{posicion["ID"]},{posicion["Titulo"]},{posicion["Genero"]},{posicion["Año_de_Lanzamiento"]},{posicion["Duracion"]},{posicion["ATP"]},{plataformas}"
        archivo.write(formato_guardar)
    archivo.close()