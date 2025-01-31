vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    vetor.append(valor)

contador_impares = 0
for valor in vetor:
    if valor % 2 != 0:
        contador_impares += 1

print(f"\nQuantidade de valores ímpares no vetor: {contador_impares}")