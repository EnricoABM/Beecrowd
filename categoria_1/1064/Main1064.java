public class Main1064 {
    public static void main (String[] args) {
        int qntPositivos = 0;

        double soma = 0,
                valor,
                media = 0;

        java.util.Scanner input = new java.util.Scanner(System.in); // useLocale(Locale.US);

        for (int i = 0; i < 6; i++) {
            valor = input.nextDouble();
            if (valor > 0) {
                qntPositivos++;
                soma += valor;
            }
        }
        media = soma / qntPositivos;

        System.out.printf("%d valores positivos\n", qntPositivos);
        System.out.printf("%.1f\n", media);
    }
}