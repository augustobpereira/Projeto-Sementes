numero1 = float(input("Digite o primeiro número: "))

while True:
    numero2 = float(input("Digite o segundo número (não pode ser zero): "))

    if numero2 != 0:
        break
    else:
        print("O divisor não pode ser zero! Digite um valor válido.\n")

resultado = numero1 / numero2
print(f"\nO resultado da divisão de {numero1} por {numero2} é: {resultado:.2f}")
