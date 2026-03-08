class BibliotecaServicio:
    def __init__(self):
        # Diccionario: clave = ISBN, valor = Objeto Libro
        self.libros_disponibles = {}
        # Diccionario: clave = ID Usuario, valor = Objeto Usuario
        self.usuarios_registrados = {}
        # Conjunto para asegurar IDs de usuario únicos
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido exitosamente.")
        else:
            print("Error: El ISBN ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Error: Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("Error: El ID de usuario ya está en uso.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            # Opcional: Validar que no tenga libros pendientes
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("Error: Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn) # Se quita de disponibles
            self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {self.usuarios_registrados[id_usuario].nombre}.")
        else:
            print("Error: Libro o Usuario no disponible.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto.")
                    return
            print("Error: El usuario no tiene ese libro.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                encontrados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                encontrados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                encontrados.append(libro)
        return encontrados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            return self.usuarios_registrados[id_usuario].libros_prestados
        return None