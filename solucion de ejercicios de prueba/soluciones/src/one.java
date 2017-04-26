
import java.util.Scanner;

public class one {

    public static void main(String[] args) {
        Scanner datos = new Scanner(System.in);
        int a = datos.nextInt();
        for (int i = 0; i < a; i++) {
            String cadena = datos.next();
            if (cadena.length() == 5) {
                System.out.println("3");
                continue;
            }
            if ((cadena.charAt(0) == 'o' && cadena.charAt(1) == 'n') || (cadena.charAt(1) == 'n' && cadena.charAt(2) == 'e') || (cadena.charAt(2) == 'e' && cadena.charAt(0) == 'o')) {
                System.out.println("1");
            } else {
                System.out.println("2");
            }

        }
    }
}
