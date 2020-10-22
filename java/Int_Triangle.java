import java.util.Scanner;

public class Int_Triangle {

	static int[][] data = new int[500][500];
	static int[][] dp = new int[500][500];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<=i; j++) {
				data[i][j] = sc.nextInt();
				dp[i][j] = data[i][j];
			}
		}
		
		int res = 0;
		for(int i=1; i<n; i++) {
			for(int j=0; j<=i; j++) {
				int left, right;
				if(j==0) left=0;
				else left= dp[i-1][j-1];
				if(j==i) right=0;
				else right = dp[i-1][j];
				dp[i][j] = dp[i][j] + Math.max(left, right);
				res = Math.max(dp[i][j], res);
			}
		}
		
		System.out.println(res);
		
	}

}
