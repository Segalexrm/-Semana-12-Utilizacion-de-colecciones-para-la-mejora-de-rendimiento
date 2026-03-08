from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():
    servicio = BibliotecaServicio()

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA DIGITAL ---")
        print("1. Añadir Libro")
        print("2. Registrar Usuario")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Buscar Libro")
        print("6. Listar Libros Prestados")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            t = input("Título: ");
            a = input("Autor: ")
            c = input("Categoría: ");
            i = input("ISBN: ")
            servicio.añadir_libro(Libro(t, a, c, i))

        elif opcion == "2":
            n = input("Nombre: ");
            id_u = input("ID Usuario: ")
            servicio.registrar_usuario(Usuario(n, id_u))

        elif opcion == "3":
            isbn = input("ISBN del libro: ");
            id_u = input("ID Usuario: ")
            servicio.prestar_libro(isbn, id_u)

        elif opcion == "4":
            isbn = input("ISBN del libro: ");
            id_u = input("ID Usuario: ")
            servicio.devolver_libro(isbn, id_u)

        elif opcion == "5":
            print("Buscar por: 1. Titulo, 2. Autor, 3. Categoria")
            c_op = input("Opción: ")
            criterios = {"1": "titulo", "2": "autor", "3": "categoria"}
            valor = input("Texto a buscar: ")
            res = servicio.buscar_libro(criterios.get(c_op, "titulo"), valor)
            for l in res: print(l)

        elif opcion == "6":
            id_u = input("ID Usuario: ")
            libros = servicio.listar_libros_prestados(id_u)
            if libros:
                for l in libros: print(l)
            else:
                print("No tiene libros o usuario no existe.")

        elif opcion == "7":
            break


if __name__ == "__main__":
    menu()