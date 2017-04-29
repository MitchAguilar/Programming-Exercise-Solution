package pkg11942;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[10];
        int casos = sc.nextInt();
        boolean inicil = true;
        for (int i = 0; i < casos; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[j] = sc.nextInt();
            }
            if (inicil) {
                System.out.println("Lumberjacks:");
                inicil = false;
            }
            if (arr[0] > arr[1] && arr[1] > arr[2] && arr[2] > arr[3] && arr[3] > arr[4] && arr[4] > arr[5] && arr[5] > arr[6] && arr[6] > arr[7] && arr[7] > arr[8] && arr[8] > arr[9]) {
                System.out.println("Ordered");
            } else if (arr[0] < arr[1] && arr[1] < arr[2] && arr[2] < arr[3] && arr[3] < arr[4] && arr[4] < arr[5] && arr[5] < arr[6] && arr[6] < arr[7] && arr[7] < arr[8] && arr[8] < arr[9]) {
                System.out.println("Ordered");
            } else {
                System.out.println("Unordered");
            }
        }
    }
}
