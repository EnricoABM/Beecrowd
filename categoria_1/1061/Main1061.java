public class Main1061 {
    public static void main (Strings[] args) {
                
        int first_day, 
            first_hour, 
            first_minutes, 
            first_seconds,
            first_total_seconds;
        
        int final_day, 
            final_hour, 
            final_minutes, 
            final_seconds,
            final_total_seconds;
        
        int total_seconds;
        
        int W,
            X,
            Y,
            Z;
        
        Scanner input = new Scanner(System.in);
        
        input.next();
        first_day = input.nextInt();
        
        first_hour = input.nextInt();
        input.next();
        first_minutes = input.nextInt();
        input.next();
        first_seconds = input.nextInt();
        
        input.next();
        final_day = input.nextInt();
        
        final_hour = input.nextInt();
        input.next();
        final_minutes = input.nextInt();
        input.next();
        final_seconds = input.nextInt();
        
        
        first_total_seconds = first_day * 86400 + 
                first_hour * 3600 + 
                first_minutes * 60 + 
                first_seconds;
        
        final_total_seconds = final_day * 86400 + 
                final_hour * 3600 + 
                final_minutes * 60 + 
                final_seconds;
        
        total_seconds = final_total_seconds - first_total_seconds;
        
        W = total_seconds / 86400;
        total_seconds %= 86400;
        X = total_seconds / 3600;
        total_seconds %= 3600;
        Y = total_seconds / 60;
        total_seconds %= 60;
        Z = total_seconds;
        
        System.out.printf("%d dia(s)\n", W);
        System.out.printf("%d hora(s)\n", X);
        System.out.printf("%d minuto(s)\n", Y);
        System.out.printf("%d segundo(s)\n", Z); 
    }
}