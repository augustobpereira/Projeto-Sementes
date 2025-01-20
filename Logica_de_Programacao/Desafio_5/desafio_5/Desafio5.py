def calcular_comissao(valor_imovel):

    if valor_imovel >= 50000:
        comissao = valor_imovel * 0.20  # 20% de comissão
    elif valor_imovel >= 30000:
        comissao = valor_imovel * 0.15  # 15% de comissão
    else:
        comissao = valor_imovel * 0.10  # 10% de comissão
    return comissao

def main():
    print('-------------------------------')
    print("Bem-vindo ao sistema de comissão de vendas!")
    print('-------------------------------\n')

    nome_vendedor = input("Informe o nome do vendedor: ")
    valor_imovel = float(input("Informe o valor do imóvel a ser vendido (R$): "))

    comissao = calcular_comissao(valor_imovel)

    # Exibe as informações solicitadas
    print("\nResumo da venda:")
    print(f"Vendedor: {nome_vendedor}")
    print(f"Valor do imóvel: R$ {valor_imovel:.2f}")
    print(f"Comissão: R$ {comissao:.2f}")

if __name__ == "__main__":
    main()