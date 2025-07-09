# main.py

from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Criar livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "12345")
    livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937, "67890")
    livro3 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "54321")

    # Adicionar livros
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Listar livros
    biblioteca.listar_livros()

    # Buscar livro pelo título
    biblioteca.buscar_livro_por_titulo("Vermelho,Branco e Sangue Azul")

    # Remover livro pelo ISBN
    biblioteca.remover_livro_por_isbn("67890")

    # Listar livros novamente para verificar remoção
    biblioteca.listar_livros()

if __name__ == "__main__":
    main()
