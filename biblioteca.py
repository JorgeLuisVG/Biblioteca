print("Biblioteca")
Biblioteca = {}
def Libro():
    informacion ={}
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

    nombreLibro = input("ingrese elnombre del libro")
    nombreAutor = input("Ingrese el nombre del autor")
    genero = generoLibro()
    año = int(input("Ingrese el año de publicacion"))

    informacion[nombreLibro] = {
        "Autor" : nombreAutor,
        "Genero" : genero,
        "Año" : año
    }
    return informacion

def MostrarBiblioteca():
    for Titulo in Biblioteca.items():
        print(f"titulo : {Titulo}")

def BuscarLibro(Busqueda):
    for buscar in Biblioteca:
        if Busqueda in buscar["Titulo"]:
            print(f"{buscar}")    

while True:
    print("1 = Agregar libro")
    print("2 = Mostrar biblioteca")
    print("3 = Buscar un libro")
    print("4 = Salir")
    opcion = input()

    if opcion == "1":
        Biblioteca = {"Libro" : Libro()}
    elif opcion == "2":
        MostrarBiblioteca()
    elif opcion == "3":
        Busqueda = input("Ingrese el nombre del libro que desea buscar")
        BuscarLibro(Busqueda)
    elif opcion == "4":
        break