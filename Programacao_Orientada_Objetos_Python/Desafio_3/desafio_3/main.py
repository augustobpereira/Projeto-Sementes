from agenda_telefonica import Contato, AgendaTelefonica

def menu():
    agenda = AgendaTelefonica()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Atualizar Contato")
        print("5. Listar Contatos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            contato = Contato(nome, telefone)
            agenda.adicionarContato(contato)

        elif opcao == "2":
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.removerContato(nome)

        elif opcao == "3":
            nome = input("Digite o nome do contato a ser buscado: ")
            contato = agenda.buscarContato(nome)
            if contato:
                print(contato)

        elif opcao == "4":
            nome = input("Digite o nome do contato a ser atualizado: ")
            telefone = input("Digite o novo telefone: ")
            novoContato = Contato(nome, telefone)
            agenda.atualizarContato(nome, novoContato)

        elif opcao == "5":
            agenda.listarContatos()

        elif opcao == "6":
            print("Saindo da agenda telefônica")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()