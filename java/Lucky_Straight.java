import java.util.Scanner;

public class Lucky_Straight {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		char[] c = s.toCharArray();
		
		int sum = 0;
		for(int i=0; i<c.length; i++) {
			if(i< c.length/2) {
				sum+= c[i]-'0';
			} else {
				sum-= c[i]-'0';
			}
		}
		
		if(sum==0) {
			System.out.println("LUCKY");
		}else {
			System.out.println("READY");
		}
	}

}
