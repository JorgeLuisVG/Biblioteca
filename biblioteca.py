print("Biblioteca")

#título, autor, género, año

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
    nombreLibro = input("ingrese elnombre del libro")
    nombreAutor = input("Ingrese el nombre del autor")
    genero = generoLibro()
    año = int(input("Ingrese el año de publicacion"))

    informacion = {
        "Titulo" : nombreLibro,
        "Autor" : nombreAutor,
        "Genero" : genero,
        "Año" : año
    }


    

Libros = []

while True:
    print("1 = Agregar libro")
    opcion = input()

    if opcion == "1":
        nombre = ""
