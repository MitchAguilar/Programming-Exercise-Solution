
import java.util.Scanner;
public class Uva_11044 {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int b=a.nextInt();
        while (b!=0){
            --b;
            int c=a.nextInt();
            int d=a.nextInt();
            c/=3;
            d/=3;
            System.out.println(c*d);
        }
    }
    
}
