from peliculas import *
from manipulacion_archivos import *

def iniciar_app() -> None:
    lista_peliculas = []
    ultimo_ordenamiento = []
    
    lista_peliculas = cargar_peliculas()
    
    flag = True


    while flag:
        print("""
        1. Dar de alta
        2. Modificar
        3. Eliminar
        4. Mostrar Peliculas
        5. Ordenar Peliculas
        6. Buscar pelicula por titulo
        7. Calcular promedio
        8. Calcular porcentaje
        9. Mostrar por genero
        10. Salir
        """)
        seleccion = input("Elije una opcion: ")
        match seleccion:
            case "1":
                print(crear_pelicula(lista_peliculas))
            case "2":
                pelicula_seleccionada = input("Que pelicula quieres modificar?")
                print(modificar_pelicula(lista_peliculas,pelicula_seleccionada))
            case "3":
                pelicula_seleccionada = input("Que pelicula quieres eliminar?")
                print(eliminar_pelicula(lista_peliculas,pelicula_seleccionada))
            case "4":
                print(mostrar_peliculas(lista_peliculas))
            case "5":
                ultimo_ordenamiento = ordenar_peliculas(lista_peliculas)
            case "6":
                pelicula_seleccionada = input("Que pelicula quieres buscar?")
                print(buscar_pelicula_titulo(lista_peliculas,pelicula_seleccionada))
            case "7":
                print(calcular_promedio(lista_peliculas))
            case "8":
                print(calcular_porcentaje(lista_peliculas))
            case "9":
                mostrar_por_genero(lista_peliculas)
            case "10":
                if len(ultimo_ordenamiento) > 0:
                    guardar_peliculas(ultimo_ordenamiento)
                else:
                    guardar_peliculas(lista_peliculas)
                break
            case _:
                print("Opcion no valida")

iniciar_app()
