import java.util.Scanner;

public class Desafio_13 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        String[] nomes = new String[10];
        String nomeBusca;
        boolean encontrado = false;

        System.out.println("Digite 10 nomes:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Nome " + (i + 1) + ": ");
            nomes[i] = entrada.nextLine();
        }

        System.out.print("Digite o nome para buscar: ");
        nomeBusca = entrada.nextLine();

        for (int i = 0; i < 10; i++) {
            if (nomes[i].equalsIgnoreCase(nomeBusca)) {
                encontrado = true;
                break;
            }
        }

        if (encontrado) {
            System.out.println("Achei");
        } else {
            System.out.println("Não achei");
        }

        entrada.close();
    }
}