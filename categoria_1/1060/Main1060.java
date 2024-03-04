import java.util.Locale;
import java.util.Scanner;

public class Main1060 {
 
    public static void main(String[] args) {
        double valor;
        int cont_positivos = 0;
        Scanner entrada = new Scanner(System.in);  //.useLocale(Locale.US);
        for (int rep = 0; rep < 6; rep++) {
            valor = entrada.nextDouble();
            if (valor >= 0) {
                cont_positivos++;
            }
        }
        System.out.println( cont_positivos + " valores positivos");
    }
 
}