while True:
    numero = int(input("Digite um número entre 1 e 10: "))

    if 1 <= numero <= 10:
        break
    else:
        print("Valor inválido! Digite um número entre 1 e 10.\n")

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")