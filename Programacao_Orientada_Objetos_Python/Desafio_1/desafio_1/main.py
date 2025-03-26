from mercado import Mercado

arquivo_json = "produtos.json"

mercado = Mercado(arquivo_json)
mercado.carregar_produtos()

while True:
    opcao = input("\nDeseja adicionar um novo produto? (s/n): ").strip().lower()
    if opcao == "s":
        mercado.cadastrar_produto()
    elif opcao == "n":
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

mercado.listar_estoque()