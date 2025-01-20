def calcular_status(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def main():
    print('-------------------------------')
    print("Bem vindo ao sistema de cálculo de notas!")
    print('-------------------------------')

    # Recebendo as notas do aluno
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Informe a {i}ª nota do aluno: "))
        notas.append(nota)

    print('-------------------------------\n')

    # Calculando a média
    media = sum(notas) / len(notas)

    # Determinando o status do aluno
    status = calcular_status(media)

    # Exibindo o resultado
    print("Resultado:")
    notas_formatadas = ", ".join(
        f"{i}ª nota: {nota:.2f}" for i, nota in enumerate(notas, start=1)
    )
    print(f"Notas: {notas_formatadas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()