import java.util.Scanner;

public class Desafio_9 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        double valor1, valor2;
        double resultado;

        System.out.print("Digite o primeiro valor: ");
        valor1 = entrada.nextDouble();

        do {
            System.out.print("Digite o segundo valor: ");
            valor2 = entrada.nextDouble();

            if (valor2 == 0) {
                System.out.println("Valor inválido. Digite um valor diferente de zero.");
            }
        } while (valor2 == 0);

        resultado = valor1 / valor2;

        System.out.println("O resultado da divisão é: " + resultado);

        entrada.close();
    }
}