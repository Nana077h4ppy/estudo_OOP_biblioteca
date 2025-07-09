# biblioteca.py

from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def remover_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f"Livro com ISBN '{isbn}' removido com sucesso!")
                return
        print(f"Nenhum livro com ISBN '{isbn}' foi encontrado.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
            return
        print("\nLista de livros na biblioteca:")
        for livro in self.livros:
            print("----------------------")
            print(livro)

    def buscar_livro_por_titulo(self, palavra):
        resultados = [livro for livro in self.livros if palavra.lower() in livro.titulo.lower()]
        if resultados:
            print(f"\nLivros encontrados com '{palavra}':")
            for livro in resultados:
                print("----------------------")
                print(livro)
        else:
            print(f"Nenhum livro encontrado com '{palavra}'.")
