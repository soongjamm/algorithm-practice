import java.util.Scanner;

public class Ugly_Number {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[] ugly = new int[n];
		ugly[0] = 1;
		int i2 = 0, i3 = 0, i5 = 0; // 2, 3, 5 각 수에 대해서 몇번째 인덱스까지 처리했는지 기
		int next2 = 2, next3 = 3, next5 = 5;
		
		for(int i=1; i<n; i++) {
			ugly[i] = Math.min(next2, Math.min(next3, next5));
			// ugly[i]에 가장 작은 결과값을 넣어줬으니, 가장 작은 결과값이 들어있던 변수에 새로운 수를 곱해준다.
			if(ugly[i] == next2) {
				i2 += 1;
				next2 = ugly[i2] * 2;
			}
			if(ugly[i] == next3) {
				i3 += 1;
				next3 = ugly[i3] * 3;
			}
			if(ugly[i] == next5) {
				i5 += 1;
				next5 = ugly[i5] * 5;
			}
		}
		
		System.out.println(ugly[n-1]);
		
	}

}
