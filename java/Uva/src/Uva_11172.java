
import java.util.Scanner;

public class Uva_11172 {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int b = a.nextInt();
        while (b != 0) {
            --b;
            int c = a.nextInt();
            int d = a.nextInt();
            if (c > d) {
                System.out.println(">");
            } else if (c < d) {
                System.out.println("<");
            } else {
                System.out.println("=");
            }
        }
    }

}
