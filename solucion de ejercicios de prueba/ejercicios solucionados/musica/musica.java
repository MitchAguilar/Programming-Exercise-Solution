
import java.util.Scanner;

public class musica {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a[] = new int[8];
        for (int i = 0; i < 8; i++) {
            a[i] = s.nextInt();
        }
        if (a[0] > a[1] && a[1] > a[2] && a[2] > a[3] && a[3] > a[4] && a[4] > a[5] && a[5]>a[6] && a[6] > a[7]) {
            System.out.println("descending");
        } else if (a[0] < a[1] && a[1] < a[2] && a[2] < a[3] && a[3] < a[4] && a[4] < a[5]&& a[5]< a[6]  && a[6] < a[7]) {
            System.out.println("ascending");
        } else {
            System.out.println("mixed");
        }

    }

}
