import json
from produto import Produto

class Mercado:
    def __init__(self, arquivo_json):
        self.produtos = []
        self.arquivo_json = arquivo_json
        self.ultimo_id = 0  # Inicia o ID como 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def carregar_produtos(self):
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as file:
                dados = json.load(file)
                if dados:
                    for item in dados:
                        produto = Produto(item["id"], item["nome"], item["quantidade"], item["preco"])
                        self.adicionar_produto(produto)
                        self.ultimo_id = max(self.ultimo_id, item["id"])
        except FileNotFoundError:
            print("Cadastro de estoque de produtos não encontrado. Criando novo estoque.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")

    def listar_estoque(self):
        print("\nEstoque do mercado:\n")
        for produto in self.produtos:
            print(produto)

        valor_total = sum(produto.calcular_subtotal() for produto in self.produtos)
        print(f"\nValor total em produtos no mercado: R$ {valor_total:.2f}")

    def cadastrar_produto(self):
        try:
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))

            self.ultimo_id += 1
            novo_produto = Produto(self.ultimo_id, nome, quantidade, preco)
            self.adicionar_produto(novo_produto)

            self.salvar_produtos()
            print(f"\nProduto '{nome}' adicionado e salvo com sucesso!\n")

        except ValueError:
            print("Erro: Certifique-se de inserir valores numéricos corretamente.")

    def salvar_produtos(self):
        try:
            with open(self.arquivo_json, "w", encoding="utf-8") as file:
                json.dump([vars(produto) for produto in self.produtos], file, indent=4, ensure_ascii=False)
            print("Produtos salvos no arquivo JSON com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar no arquivo JSON os produtos: {e}")