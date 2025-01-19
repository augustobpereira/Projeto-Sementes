def calcular_desconto(quantidade, preco):
    if quantidade <= 10:
        desconto = 0  # NÃO POSSUI DESCONTO
    elif 11 <= quantidade <= 20:
        desconto = 0.10  # 10% DE DESCONTO
    elif 21 <= quantidade <= 50:
        desconto = 0.20  # 20% DE DESCONTO
    else:
        desconto = 0.25  # 25% DE DESCONTO

    subtotal = quantidade * preco
    valor_com_desconto = subtotal * (1 - desconto)
    return desconto, valor_com_desconto


def main():
    print("Bem-vindo ao sistema de compras do mercado!\n")
    produtos = []

    while True:
        nome = input("Informe o nome do produto (ou digite 'sair' para finalizar): ")
        if nome.lower() == "sair":
            break

        preco = float(input(f"Informe o preço do produto '{nome}': R$ "))
        quantidade = int(input(f"Informe a quantidade de '{nome}': "))

        produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        print("\n")

    # EXIBINDO OS DETALHES DOS PRODUTOS E CALCULANDO O TOTAL GERAL
    print("\nResumo da Compra:")
    valor_total_geral = 0

    for produto in produtos:
        desconto, valor_com_desconto = calcular_desconto(
            produto["quantidade"], produto["preco"]
        )
        valor_total_geral += valor_com_desconto

        # EXIBE O SUBTOTAL
        detalhes = (
            f"- {produto['nome']}: {produto['quantidade']} unidade(s) x R$ {produto['preco']:.2f} "
            f"= R$ {produto['quantidade'] * produto['preco']:.2f}"
        )
        # INCLUI O DESCONTO SOMENTE SE APLICÁVEL
        if desconto > 0:
            detalhes += f" (Desconto: {desconto * 100:.0f}%, Total com desconto: R$ {valor_com_desconto:.2f})"
        print(detalhes)

    # EXIBINDO O TOTAL GERAL
    print(f"\nValor total a pagar: R$ {valor_total_geral:.2f}")

if __name__ == "__main__":
    main()