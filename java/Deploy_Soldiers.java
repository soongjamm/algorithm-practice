import java.util.Scanner;

public class Deploy_Soldiers {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[] data = new int[n];
		int[] dp = new int[n];
		for(int i=n-1; i>=0; i--) data[i] = sc.nextInt();
		for(int i=0; i<n; i++) dp[i] = 1;
		
		int max = 1; // 값이 변하지 않는 경우. 최소 길이 1
		for(int i=1; i<n; i++) {
			for(int j=0; j<i; j++) {
				if(data[i]>data[j]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
					if(dp[i]>max) max = dp[i];
				}
			}
		}
		System.out.println(n-max);
		
	}

}
