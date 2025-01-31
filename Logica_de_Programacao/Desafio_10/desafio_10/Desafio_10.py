while True:

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"\nA média do aluno é: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado! \n")
    else:
        print("Situação: Reprovado. \n")

    repetir = input("Deseja calcular a média de outro aluno? (s/n): ").strip().lower()
    if repetir != "s":
        print("Calculo encerrado. Até mais!")
        break