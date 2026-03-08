class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Almacenamos título y autor en una tupla (inmutable) como pide el requisito
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} [Categoría: {self.categoria}, ISBN: {self.isbn}]"