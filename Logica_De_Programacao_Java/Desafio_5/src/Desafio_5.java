import java.util.Scanner;

public class Desafio_5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o nome do vendedor: ");
        String nomeVendedor = scanner.nextLine();

        System.out.print("Digite o valor do imóvel: ");
        double valorImovel = scanner.nextDouble();

        double comissao = 0;
        double porcentagem = 0;

        if (valorImovel >= 50000) {
            comissao = valorImovel * 0.20;
            porcentagem = 20;
        } else if (valorImovel >= 30000) {
            comissao = valorImovel * 0.15;
            porcentagem = 15;
        } else {
            comissao = valorImovel * 0.10;
            porcentagem = 10;
        }

        System.out.println("Nome do vendedor: " + nomeVendedor);
        System.out.println("Valor do imóvel: R$ " + valorImovel);
        System.out.println("Comissão: R$ " + comissao + " (" + porcentagem + "%)");

        scanner.close();
    }
}