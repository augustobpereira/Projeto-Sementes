import java.text.Normalizer;
import java.util.Scanner;

public class Desafio_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha a bebida (Cerveja, Refrigerante, Água): ");
        String bebida = removerAcentos(scanner.nextLine().trim());

        if (bebida.equalsIgnoreCase("cerveja")) {
            if (verificarIdade(scanner)) {
                System.out.println("Compra efetuada com sucesso!");
            } else {
                System.out.println("Compra negada");
            }
        } else if (bebida.equalsIgnoreCase("refrigerante") || bebida.equalsIgnoreCase("agua")) {
            System.out.println("Compra efetuada com sucesso!");
        } else {
            System.out.println("Opção inválida!");
        }

        scanner.close();
    }

    private static boolean verificarIdade(Scanner scanner) {
        System.out.println("Informe sua idade: ");
        try {
            int idade = Integer.parseInt(scanner.nextLine().trim());
            return idade >= 18;
        } catch (NumberFormatException e) {
            System.out.println("Idade inválida! Digite um número.");
            return false;
        }
    }

    private static String removerAcentos(String str) {
        String normalizado = Normalizer.normalize(str, Normalizer.Form.NFD);
        return normalizado.replaceAll("[^\\p{ASCII}]", "");
    }
}
