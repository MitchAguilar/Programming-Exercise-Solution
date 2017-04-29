package ejercicio10055;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ejercicio10055 {

    public static void main(String[] args) {

        BufferedReader tec = new BufferedReader(new InputStreamReader(System.in));
        String cadena = "";
        try {
            while (!(cadena = tec.readLine()).isEmpty()) {
                String data[] = cadena.split(" ");
                int res = Math.abs(Integer.parseInt(data[0]) - Integer.parseInt(data[1]));
                System.out.println(res);
            }
        } catch (Exception ex) {

        }
    }
}
