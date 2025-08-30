import java.util.Scanner;

public class HargaEmas {
  public static Scanner input = new Scanner(System.in);

  public static long hargaEmas(String N, String C, int[] W, int[] V) {
    int cnt = Integer.parseInt(N);
    int cap = Integer.parseInt(C);
    long[] temp = new long[cap + 1];

    for (int i = 1; i <= cnt; i++) {
      for (int j = cap; j >= W[i - 1]; j--) {
        temp[j] = Math.max(temp[j], temp[j - W[i - 1]] + V[i - 1]);
      }
    }

    return temp[cap];
  }

  public static void main(String[] args) {
    String firstInput = input.nextLine();
    String[] parts = firstInput.trim().split("\\s+");
    String N = parts[0];
    String C = parts[1];
    int[] W = new int[Integer.parseInt(N)];
    int[] V = new int[Integer.parseInt(N)];

    for (int k = 0; k < Integer.parseInt(N); k++) {
      String nextInput = input.nextLine();
      String[] nextParts = nextInput.trim().split("\\s+");
      W[k] = Integer.parseInt(nextParts[0]);
      V[k] = Integer.parseInt(nextParts[1]);
    }

    System.out.println(hargaEmas(N, C, W, V));
  }
}
