
import java.util.Scanner;


public class tarifa {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int a= sc.nextInt();
        int b=sc.nextInt();
        int c=0;
        for (int i = 0; i < b; i++) {
            int d=sc.nextInt();
            c+=(a-d);
        }
        System.out.println(c+a);
    }
    
}
