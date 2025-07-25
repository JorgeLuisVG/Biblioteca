print("Biblioteca")

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

Biblioteca = {}

while True:
    print("1 = Agregar libro")
    opcion = input()

    if opcion == "1":
        Biblioteca = {"Libros" : Libro()}


