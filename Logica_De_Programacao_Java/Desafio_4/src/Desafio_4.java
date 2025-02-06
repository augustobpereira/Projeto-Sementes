import java.util.Scanner;

public class Desafio_4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        double num1 = scanner.nextDouble();

        System.out.print("Digite o segundo número: ");
        double num2 = scanner.nextDouble();

        System.out.print("Escolha a operação (+, -, *, /): ");
        char operacao = scanner.next().charAt(0);

        double resultado = 0;
        boolean operacaoValida = true;

        switch (operacao) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                if (num2 == 0) {
                    System.out.println("Erro: Divisão por zero não permitida!");
                    operacaoValida = false;
                } else {
                    resultado = num1 / num2;
                }
                break;
            default:
                System.out.println("Erro: Operação inválida!");
                operacaoValida = false;
                break;
        }

        if (operacaoValida) {
            System.out.println("Resultado: " + resultado);
        }

        scanner.close();
    }
}
