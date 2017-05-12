import java.util.Scanner;

public class notas {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        for (int i = 0; i < a; i++) {
            String b = sc.next();
            double d = 0;
            //010101001
            double c = 0;
            for (int j = 0; j < b.length(); j++) {
                try {
                    if (b.charAt(j) == '1' && b.charAt(j + 1) == '0') {
                        c += 10;
                        d++;
                        j++;
                    } else {
                        c += Integer.parseInt(b.charAt(j) + "");
                        d++;

                    }
                } catch (Exception e) {
                    d++;
                    c += Integer.parseInt(b.charAt(j) + "");
                }
            }
            double e = (c / d);
            System.out.printf("%.2f\n", e);
        }

    }
}
