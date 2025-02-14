import java.util.Arrays;
import java.util.Scanner;

public class Desafio_14 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        String[] nomes = new String[20]; // Cria um vetor de 20 Strings

        System.out.println("Digite 20 nomes:");
        for (int i = 0; i < 20; i++) {
            System.out.print("Nome " + (i + 1) + ": ");
            nomes[i] = entrada.nextLine();
        }

        Arrays.sort(nomes);

        String[] nomesSemRepeticao = new String[20];
        int novoTamanho = 0;

        for (int i = 0; i < 20; i++) {
            boolean repetido = false;

            for (int j = 0; j < novoTamanho; j++) {
                if (nomes[i].equals(nomesSemRepeticao[j])) {
                    repetido = true;
                    break;
                }
            }

            if (!repetido) {
                nomesSemRepeticao[novoTamanho] = nomes[i];
                novoTamanho++;
            }
        }

        System.out.println("\nNomes sem repetição:");
        for (int i = 0; i < novoTamanho; i++) {
            System.out.println(nomesSemRepeticao[i]);
        }

        entrada.close();
    }
}