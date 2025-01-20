def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

def main():
    print('-------------------------------')
    print("Bem-vindo à calculadora!")
    print('-------------------------------\n')

    print("Selecione a operação que deseja realizar:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)\n")

    operacao = input("Digite o número da operação escolhida: ")

    try:
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        match operacao:
            case "1":
                resultado = adicao(num1, num2)
                simbolo = "+"
            case "2":
                resultado = subtracao(num1, num2)
                simbolo = "-"
            case "3":
                resultado = multiplicacao(num1, num2)
                simbolo = "*"
            case "4":
                resultado = divisao(num1, num2)
                simbolo = "/"
            case _:
                print("\nOperação inválida. Tente novamente.")
                return

        # Mostra o resultado
        print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")

    except ValueError:
        print("\nErro: Por favor, insira números válidos.")

    print("\nObrigado por usar a calculadora!")

if __name__ == "__main__":
    main()