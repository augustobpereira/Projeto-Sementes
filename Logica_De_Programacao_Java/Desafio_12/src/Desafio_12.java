import java.util.Scanner;

public class Desafio_12 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int[] vetor = new int[10];
        int quantidadeImpares = 0;

        System.out.println("Digite 10 valores inteiros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Valor " + (i + 1) + ": ");
            vetor[i] = entrada.nextInt();
        }

        for (int i = 0; i < 10; i++) {
            if (vetor[i] % 2 != 0) {
                quantidadeImpares++;
            }
        }

        System.out.println("Quantidade de valores ímpares no vetor: " + quantidadeImpares);
        entrada.close();
    }
}