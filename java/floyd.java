import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class floyd {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] dist = new int[n][n];
		
		int INF = (int)1e9;
		for(int i=0; i<n; i++) {
			Arrays.fill(dist[i], INF);
		}
		
		for(int i=0; i<m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			dist[a-1][b-1] = Math.min(dist[a-1][b-1], c);
		}
		
		for(int k=0; k<n; k++) {
			for(int a=0; a<n; a++) {
				for(int b=0; b<n; b++) {
					if(a==b) dist[a][b]=0;
					else dist[a][b] = Math.min(dist[a][k]+dist[k][b], dist[a][b]);
				}
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(dist[i][j]!=INF) System.out.printf("%d ", dist[i][j]);
				else System.out.printf("%d ", 0);
			}
			System.out.println();
		}
		
	}

}
