import java.util.Scanner;

public class Retire {
	
	static int[] t = new int[1001];
	static int[] p = new int[1001];
	static int[] d = new int[1001];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for(int i=0; i<n; i++) {
			t[i] = sc.nextInt();
			p[i] = sc.nextInt();
		}
		
		int max_value = 0;
		for(int i=n-1; i>=0; i--) {
			if( t[i] + i <= n ) {
				d[i] = Math.max(d[i+t[i]] + p[i], max_value);
				max_value = d[i];
			} else {
				d[i] = max_value;
			}
		}
		
		System.out.println(max_value);
	}

}
