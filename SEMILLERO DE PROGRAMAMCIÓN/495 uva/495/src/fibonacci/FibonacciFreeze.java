package fibonacci;

import java.math.BigInteger;
import java.util.Scanner;

public class FibonacciFreeze {

    public static void main(String[] args) {
        Scanner dato = new Scanner(System.in);
        int a = 0;
        while ((a = dato.nextInt()) >= 0) {
            BigInteger b1 = new BigInteger("0");
            BigInteger b2 = new BigInteger("1");
            BigInteger b3 = new BigInteger("0");
            for (int i = 0; i < (a - 1); i++) {
                b3 = b1.add(b2);
                b1 = b2;
                b2 = b3;
            }
            System.out.printf("The Fibonacci number for %d is %s\n",a, b2);
        }
    }
}
