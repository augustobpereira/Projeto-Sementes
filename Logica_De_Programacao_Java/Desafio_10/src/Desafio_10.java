import java.util.Scanner;

public class Desafio_10 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        double nota1, nota2, media;
        char continuar;

        do {
            System.out.print("Digite a primeira nota: ");
            nota1 = entrada.nextDouble();
            System.out.print("Digite a segunda nota: ");
            nota2 = entrada.nextDouble();

            media = (nota1 + nota2) / 2;

            System.out.println("A média do aluno é: " + media);

            if (media >= 7) {
                System.out.println("Aluno aprovado!");
            } else {
                System.out.println("Aluno reprovado.");
            }

            System.out.print("Deseja calcular outra média? (s/n): ");
            continuar = entrada.next().charAt(0);
        } while (continuar == 's' || continuar == 'S');

        System.out.println("Programa encerrado.");
        entrada.close();
    }
}