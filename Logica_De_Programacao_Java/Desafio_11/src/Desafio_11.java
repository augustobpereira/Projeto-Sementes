import java.util.Scanner;

public class Desafio_11 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        String usuario, senha;
        int tentativas = 0; // Variável para contar as tentativas

        do {
            System.out.print("Digite o usuário: ");
            usuario = entrada.nextLine();
            System.out.print("Digite a senha: ");
            senha = entrada.nextLine();

            if (usuario.equals("aluno") && senha.equals("segredo")) {
                System.out.println("Bem vindo!");
                break;
            } else {
                tentativas++;
                System.out.println("Login incorreto. Tente novamente.");

                if (tentativas >= 3) {
                    System.out.println("Usuário bloqueado. Número de tentativas excedido.");
                    break;
                }
            }
        } while (true);

        entrada.close();
    }
}