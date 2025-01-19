import json

# Local dentro do Projeto onde esta salvo o arquivo JSON
arquivo_json = "desafio_1/produtos.json"

# Lendo todos os dados contidos dentro do arquivo JSON:
with open(arquivo_json, "r", encoding="utf-8") as DadosJson:
    produtos = json.load(DadosJson)

# Iniciando a variável o valor total
valor_total = 0

# Verificando linha por linha pelos produtos e calculando o valor total:
print("Informações dos produtos no mercado:\n")
for produto in produtos:
    subtotal = produto["quantidade"] * produto["preco"]
    valor_total += subtotal
    print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}, Subtotal: R$ {subtotal:.2f}")

# Exibindo o resultado da soma de todos os produtos:
print("\nValor total em produtos no mercado: R$ {:.2f}".format(valor_total))