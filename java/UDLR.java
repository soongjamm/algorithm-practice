import java.util.Scanner;
import java.util.StringTokenizer;

public class UDLR {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		String s = sc.nextLine();
		String[] c = s.split(" ");
		
		int x = 1;
		int y = 1;
		
		// 동, 서, 북, 남
		int[] dx = {0, 0, 1, -1};
		int[] dy = {1, -1, 0, 0};
		for(int i=0; i< c.length ; i++) {
			int k = -1;
			if( c[i].equals("R")) k=0;
			if( c[i].equals("L") ) k=1;
			if( c[i].equals("D") ) k=2;
			if( c[i].equals("U") ) k=3;
			int nx=x+dx[k], ny=y+dy[k];
			
			if( 1 <= nx && nx <= n && 1 <= ny && ny <= n) {
				x = nx;
				y = ny;
			}
		}
		
		System.out.printf("%d %d", x, y);
	}

}
