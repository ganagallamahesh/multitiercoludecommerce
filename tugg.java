import java.util.*;

public class tug {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while (T-- > 0) {

            int n = sc.nextInt();

            int[] weight = new int[n];
            int total = 0;

            for (int i = 0; i < n; i++) {
                weight[i] = sc.nextInt();
                total += weight[i];
            }

            int size1 = n / 2;
            int size2 = n - size1;

            boolean[][] dp = new boolean[size2 + 1][total + 1];

            dp[0][0] = true;

            for (int w : weight) {

                for (int count = size2; count >= 1; count--) {

                    for (int sum = total; sum >= w; sum--) {

                        if (dp[count - 1][sum - w]) {
                            dp[count][sum] = true;
                        }
                    }
                }
            }

            int best1 = 0;
            int bestDiff = Integer.MAX_VALUE;

            for (int sum = 0; sum <= total; sum++) {

                if (dp[size1][sum]) {

                    int other = total - sum;
                    int diff = Math.abs(sum - other);

                    if (diff < bestDiff) {
                        bestDiff = diff;
                        best1 = sum;
                    }
                }

                if (dp[size2][sum]) {

                    int other = total - sum;
                    int diff = Math.abs(sum - other);

                    if (diff < bestDiff) {
                        bestDiff = diff;
                        best1 = sum;
                    }
                }
            }

            int best2 = total - best1;

            if (best1 > best2) {
                int temp = best1;
                best1 = best2;
                best2 = temp;
            }

            System.out.println(best1 + " " + best2);

            if (T > 0) {
                System.out.println();
            }
        }

        sc.close();
    }
}