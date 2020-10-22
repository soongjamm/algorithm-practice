import java.util.Scanner;

public class Edit_Dist {

		
	public static int edit_dist(String str1, String str2) {
		int n = str1.length();
		int m = str2.length();
		int[][] dp = new int[n+1][m+1];
		
		for(int i=0; i<n; i++) dp[0][i] = i;
		for(int i=0; i<m; i++) dp[i][0] = i;
		
		for(int i=1; i<=n; i++) {
			for(int j=1; j<=m; j++) {
				if(str1.charAt(i-1) == str2.charAt(j-1)) {
					dp[i][j] = dp[i-1][j-1];
				} else {
					dp[i][j] = 1 + Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1]));
				}
			}
		}
		
		return dp[n][m]; 
	}
		
	public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			String str1 = sc.nextLine();
			String str2 = sc.nextLine();
			
			System.out.println(edit_dist(str1, str2));
	}

}
