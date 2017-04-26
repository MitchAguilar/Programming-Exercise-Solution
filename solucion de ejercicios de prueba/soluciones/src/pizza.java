
import java.util.Scanner;

public class pizza {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        Scanner c= new Scanner(System.in);
        int b = a.nextInt();
        while (b != 0) {
            b--;
            int in = a.nextInt();
            String pre[] = new String[in];
            String seg[] = new String[in];
            for (int i = 0; i < in; i++) {
                pre[i] = c.nextLine();
                System.out.println("----- "+pre[i]);
            }
            for (int i = 0; i < in; i++) {
                seg[i] = c.nextLine();
                System.out.println("----- "+seg[i]);
            }
        }
    }
}
