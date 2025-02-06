import java.util.Scanner;

public class Desafio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome do produto:");
        String nomeProduto = scanner.nextLine();

        System.out.println("Digite o preço unitário do produto:");
        double preco = scanner.nextDouble();

        System.out.println("Digite a quantidade comprada:");
        int quantidade = scanner.nextInt();

        double valorTotal = preco * quantidade;
        double desconto = 0;

        if (quantidade > 50) {
            desconto = 0.25;
        } else if (quantidade >= 21) {
            desconto = 0.20;
        } else if (quantidade >= 11) {
            desconto = 0.10;
        }

        double valorComDesconto = valorTotal - (valorTotal * desconto);

        System.out.println("\nResumo da Compra:");
        System.out.println("Produto: " + nomeProduto);
        System.out.println("Quantidade: " + quantidade);
        System.out.printf("Valor Total: R$ %.2f\n", valorTotal);
        System.out.printf("Desconto aplicado: %.0f%%\n", desconto * 100);
        System.out.printf("Valor Final a Pagar: R$ %.2f\n", valorComDesconto);

        scanner.close();
    }
}