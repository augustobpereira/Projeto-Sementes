import java.util.Scanner;

public class Desafio_6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;

        while (true) {
            System.out.print("Digite um número entre 1 e 10: ");

            if (scanner.hasNextInt()) {
                numero = scanner.nextInt();

                if (numero >= 1 && numero <= 10) {
                    System.out.println("Você digitou: " + numero);

                    if (numero == 10) {
                        System.out.println("Programa encerrado.");
                        break;
                    }
                } else {
                    System.out.println("ERRO! Digite um número entre 1 e 10.");
                }
            } else {
                System.out.println("ERRO! Entrada inválida. Digite um número entre 1 e 10.");
                scanner.next();
            }
        }
        scanner.close();
    }
}