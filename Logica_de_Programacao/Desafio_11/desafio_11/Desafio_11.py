tentativas = 0 

while tentativas < 3:
    usuario = input("Digite o nome usuário: ")
    senha = input("Digite a senha do usuário: ")

    if usuario == "Augusto" and senha == "teste@123":
        print("Bem vindo!")
        break
    else:
        tentativas += 1
        print("Login inválido! Tente novamente.")

    if tentativas == 3:
        print("Usuário bloqueado por tentativas excessivas.")