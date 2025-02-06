vetor_nomes = []
for i in range(20):
    nome = input(f"Digite o {i + 1}º nome: ")
    vetor_nomes.append(nome)

vetor_unicos = []

for nome in vetor_nomes:
    if nome not in vetor_unicos:
        vetor_unicos.append(nome)

print("\nNomes únicos restantes:")
for nome in vetor_unicos:
    print(nome)
