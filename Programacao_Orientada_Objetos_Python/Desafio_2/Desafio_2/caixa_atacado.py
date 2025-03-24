import json
from produto import Produto

class CaixaDoAtacado:
    def __init__(self):
        self.produtos = {}
        self.proximo_id = 1
        self.arquivo_produtos = 'produtos.json'

    def adicionar_produto(self, produto):
        self.produtos[produto.id] = produto

    def computar_compra(self, itens_compra, metodo_pagamento):
        total_inicial = 0
        detalhes_itens = []

        for id_produto, quantidade in itens_compra:
            produto = self.produtos.get(id_produto)
            if produto:
                preco_unitario = produto.preco
                preco_total_item = preco_unitario * quantidade
                total_inicial += preco_total_item
                detalhes_itens.append((produto.nome, quantidade, preco_total_item))

        total_final = total_inicial
        desconto_quantidade = 0
        desconto_pagamento = 0

        for nome, quantidade, preco_total_item in detalhes_itens:
            if quantidade >= 5 and quantidade < 15:
                desconto = preco_total_item * 0.1
                total_final -= desconto
                desconto_quantidade += desconto
            elif quantidade >= 15 and quantidade < 25:
                desconto = preco_total_item * 0.2
                total_final -= desconto
                desconto_quantidade += desconto
            elif quantidade >= 25:
                desconto = preco_total_item * 0.25
                total_final -= preco_total_item * 0.25
                desconto_quantidade += preco_total_item * 0.25

        if metodo_pagamento == 'dinheiro':
            desconto_pagamento = total_final * 0.05
            total_final -= desconto_pagamento
        elif metodo_pagamento == 'credito':
            acrescimo_pagamento = total_final * 0.03
            total_final += acrescimo_pagamento
            desconto_pagamento = -acrescimo_pagamento

        return total_inicial, total_final, detalhes_itens, metodo_pagamento, desconto_quantidade, desconto_pagamento

    def adicionar_produto_ao_cardapio(self, nome, preco):
        produto = Produto(self.proximo_id, nome, preco)
        self.adicionar_produto(produto)
        print(f'Produto "{nome}" adicionado a lista de produtos com ID {self.proximo_id}.')
        self.proximo_id += 1
        self.salvar_produtos()

    def salvar_produtos(self):
        dados_produtos = [{'id': produto.id, 'nome': produto.nome, 'preco': produto.preco} for produto in self.produtos.values()]
        with open(self.arquivo_produtos, 'w') as arquivo:
            json.dump(dados_produtos, arquivo)

    def carregar_produtos(self):
        try:
            with open(self.arquivo_produtos, 'r') as arquivo:
                dados_produtos = json.load(arquivo)
                for dado_produto in dados_produtos:
                    produto = Produto(dado_produto['id'], dado_produto['nome'], dado_produto['preco'])
                    self.adicionar_produto(produto)
                if dados_produtos:
                    self.proximo_id = max(produto.id for produto in self.produtos.values()) + 1
        except FileNotFoundError:
            pass