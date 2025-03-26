from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n===== Gerenciador de Biblioteca =====")
        print("1 - Adicionar Livro")
        print("2 - Emprestar Livro")
        print("3 - Devolver Livro")
        print("4 - Listar Livros")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o autor do livro: ").strip()
            try:
                biblioteca.adicionar_livro(titulo, autor)
                print(f"Livro '{titulo}' adicionado com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            titulo = input("Digite o título do livro para emprestar: ").strip()
            try:
                biblioteca.emprestar_livro(titulo)
                print(f"Livro '{titulo}' emprestado com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "3":
            titulo = input("Digite o título do livro para devolver: ").strip()
            try:
                biblioteca.devolver_livro(titulo)
                print(f"Livro '{titulo}' devolvido com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "4":
            livros = biblioteca.listar_livros()
            if livros:
                print("\nLista de livros na biblioteca:")
                for livro in livros:
                    print(f"- {livro}")
            else:
                print("A biblioteca está vazia.")

        elif opcao == "5":
            print("Saindo do sistema da biblioteca.")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()