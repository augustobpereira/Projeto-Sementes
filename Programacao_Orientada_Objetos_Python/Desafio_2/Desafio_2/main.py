from caixa_atacado import CaixaDoAtacado

def exibir_cardapio(caixa):
    print('\nCardápio:')
    for produto in caixa.produtos.values():
        print(f'{produto.id} - {produto.nome}: R$ {produto.preco:.2f}')

def simular_compra(caixa):
    itens_compra = []
    while True:
        exibir_cardapio(caixa)
        if itens_compra:
            id_produto = int(input('Digite o ID do produto (0 para cancelar, 9 para finalizar): '))
        else:
            id_produto = int(input('Digite o ID do produto (0 para cancelar): '))

        if id_produto == 0:
            print('Compra cancelada.')
            return False
        elif id_produto == 9 and itens_compra:
            break

        quantidade = int(input('Digite a quantidade: '))
        itens_compra.append((id_produto, quantidade))

    print('\nForma de pagamento:')

    print('1 - Dinheiro')
    print('2 - Débito')
    print('3 - Crédito')

    opcao_pagamento = int(input('Digite a opção de pagamento: '))

    if opcao_pagamento == 1:
        metodo_pagamento = 'Dinheiro'
    elif opcao_pagamento == 2:
        metodo_pagamento = 'Débito'
    elif opcao_pagamento == 3:
        metodo_pagamento = 'Crédito'
    else:
        print('Opção de pagamento inválida.')
        return False

    total_inicial, total_final, detalhes_itens, metodo_pagamento, desconto_quantidade, desconto_pagamento = caixa.computar_compra(itens_compra, metodo_pagamento)

    print('\nDetalhes da compra:')
    for nome, quantidade, preco_total_item in detalhes_itens:
        print(f'- {nome}: {quantidade} x R$ {preco_total_item:.2f}')

    print(f'\nMetodo de pagamento: {metodo_pagamento}')
    print(f'Valor total inicial: R$ {total_inicial:.2f}')
    print(f'Desconto por quantidade: R$ {desconto_quantidade:.2f}')
    print(f'Desconto/acréscimo por pagamento: R$ {desconto_pagamento:.2f}')
    print(f'Valor total final: R$ {total_final:.2f}')

    return True

caixa = CaixaDoAtacado()
caixa.carregar_produtos()

while True:
        print('\nOpções:')
        print('1. Adicionar produto ao cardápio')
        print('2. Simular compra')
        print('3. Sair')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            nome_produto = input('Digite o nome do produto: ')
            preco_produto = float(input('Digite o preço do produto: '))
            caixa.adicionar_produto_ao_cardapio(nome_produto, preco_produto)
        elif opcao == '2':
            if simular_compra(caixa):
                print('Compra finalizada.')
                break
        elif opcao == '3':
            break
        else:
            print('Opção inválida.')