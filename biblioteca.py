print("Biblioteca")
Biblioteca = {}

def Libro():
    def generoLibro():
        print("1 = Narrativo")
        print("2 = Lirico")
        print("3 = Dramatico")
        print("4 = Didactico")
        print("5 = Ficcion")
        print("6 = Cientifico")
        print("7 = Infantil")
        print("8 = Comic")
        print("9 = Educativo")
        Seleccion = input()

        if Seleccion == "1":
            return "Narrativo"
        elif Seleccion == "2":
            return "Lirico"
        elif Seleccion == "3":
            return "Dramatico"
        elif Seleccion == "4":
            return "Didactico"
        elif Seleccion == "5":
            return "Ficcion"
        elif Seleccion == "6":
            return "Cientifico"
        elif Seleccion == "7":
            return "Infantil"
        elif Seleccion == "8":
            return "Comic"
        elif Seleccion == "9":
            return "Educativo"
        else:
            return "Desconocido"

    nombreLibro = input("Ingrese el nombre del libro: ").strip().title()
    nombreAutor = input("Ingrese el nombre del autor: ").strip().title()
    genero = generoLibro()
    año = int(input("Ingrese el año de publicación: "))

    return {
        "Titulo": nombreLibro,
        "Autor": nombreAutor,
        "Genero": genero,
        "Año": año
    }

def MostrarBiblioteca():
    if not Biblioteca:
        print("La biblioteca está vacía.")
    else:
        for titulo, datos in Biblioteca.items():
            print(f"Título: {titulo}")
            print(f"  Autor: {datos['Autor']}")
            print(f"  Género: {datos['Genero']}")
            print(f"  Año: {datos['Año']}")
            print()

def BuscarLibro(Busqueda):
    encontrado = False
    for titulo, datos in Biblioteca.items():
        if Busqueda.title() in titulo.title():
            print(f"Título: {titulo}")
            print(f"  Autor: {datos['Autor']}")
            print(f"  Género: {datos['Genero']}")
            print(f"  Año: {datos['Año']}")
            print()
            encontrado = True
    if not encontrado:
        print("Libro no encontrado.")

while True:
    print("\n1 = Agregar libro")
    print("2 = Mostrar biblioteca")
    print("3 = Buscar un libro")
    print("4 = Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        libro = Libro()
        Biblioteca[libro["Titulo"]] = {
            "Autor": libro["Autor"],
            "Genero": libro["Genero"],
            "Año": libro["Año"]
        }
    elif opcion == "2":
        MostrarBiblioteca()
    elif opcion == "3":
        Busqueda = input("Ingrese el nombre del libro que desea buscar: ")
        BuscarLibro(Busqueda)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")


