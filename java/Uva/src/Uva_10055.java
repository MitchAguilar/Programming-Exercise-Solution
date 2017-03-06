
import java.util.Scanner;

public class Uva_10055 {

    public static void main(String[] args) {
        try {
            Scanner a = new Scanner(System.in);
            long b, c, d = 0;
            String linea[];
            while ((linea= a.nextLine().split(" "))!= null) {
                b = Long.parseLong(linea[0]);
                c = Long.parseLong(linea[1]);
                d = b - c;
                System.out.println(Math.abs(d));
            }
        } catch (Exception e) {
            
        }
    }

}
