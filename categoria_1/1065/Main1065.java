import java.util.Scanner;

public class Main1065 {
    public static void main (String[] args) {
        Scanner input = new Scanner( System.in );
        int parCount = 0;
        int count = 1;
        int valor;

        while ( count <= 5 ) {
            valor = Integer.parseInt(input.nextLine());
            
            if ( valor % 2 == 0 ) {
                parCount++;
            } // fim if
            count++;
        } // fim while

        System.out.println( parCount +" valores pares");
    } // fim main
} // fim classe