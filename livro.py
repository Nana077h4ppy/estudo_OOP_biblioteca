# livro.py

class Livro:
    def __init__(self, titulo, autor, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nISBN: {self.isbn}"
