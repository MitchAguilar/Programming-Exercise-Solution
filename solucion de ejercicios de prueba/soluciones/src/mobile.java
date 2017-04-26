
import java.util.Scanner;

public class mobile {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        String data[] = new String[13];
        data[0] = "  ";
        data[1] = " .,?";
        data[2] = " abc";
        data[3] = " def";
        data[4] = " ghi";
        data[5] = " jkl";
        data[6] = " mno";
        data[7] = " pqrs";
        data[8] = " tuv";
        data[9] = " wxyz";
        data[10] = " *";
        data[12] = " #";
        int b = a.nextInt();
        while (b != 0) {
            int c = a.nextInt();
            int l[] = new int[c];
            int m[] = new int[c];
            for (int i = 0; i < c; i++) {
                l[i] = a.nextInt();
            }
            for (int i = 0; i < c; i++) {
                m[i] = a.nextInt();
            }
            String acum = "";
            for (int i = 0; i < c; i++) {
                String as=data[l[i]]+"";
                acum+=as.charAt(m[i]);
            }
            System.out.print(acum+"\n");
            b--;
        }
    }
}
