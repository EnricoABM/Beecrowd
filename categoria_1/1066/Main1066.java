import java.util.Scanner;

public class Main1066 {
    public static void main(String[] args) {
        int parCount = 0;
        int imparCount = 0;
        int posCount = 0;
        int negCount = 0;
        
        Scanner input = new Scanner( System.in );

        int valor;

        for ( int i = 1; i <= 5; i++ ) {
            valor = Integer.parseInt(input.nextLine());

            if ( valor % 2 == 0 ) {
                parCount++;
            } 
            else {
                imparCount++;
            } // fim if
            if ( valor > 0 ) {
                posCount++;
            } 
            else if (valor < 0 ) {
                negCount++;
            } // fim if

        } // fim for

        System.out.println(  parCount + " valor(es) par(es)" );
        System.out.println(  imparCount + " valor(es) impar(es)" );
        System.out.println(  posCount + " valor(es) positivo(s)" );
        System.out.println(  negCount + " valor(es) negativo(s)" );

    } // fim main    
} // fim classe
