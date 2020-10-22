import java.util.ArrayList;

public class Compress_Str {
	
	/*
	 * 익혀야 할 것 : 
	 * 삼항연산자 이용
	 * 가독성 높은 변수명 
	 * */
	public static int solution(String s) {
		int answer = s.length();
		// 1개 단위(step)부터 압축 단위를 늘려가며 확인
		for(int step=1; step<s.length()/2+1; step++) {
			String compressed = "";
			String prev = s.substring(0,step); // 앞에서부터 step 만큼의 문자열 추출
			int cnt = 1;
			// 단위(step) 크기 만큼 증가시키며 이전 문자열과 비교
			// j는 덩어리의 시작
			for(int j=step; j<s.length(); j+= step) {
				// 이전 상태와 동일하다면 압축 횟수(count) 증가
				// k는 덩어리의 시작점부터 +step까지 한 character씩 'sub'에 넣은 후 비교한다.
				String sub = "";
				for(int k=j; k<j+step; k++) {
					if(k<s.length()) sub += s.charAt(k);
				}
				if(prev.contentEquals(sub)) cnt += 1;
				// 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면) 
				else {
					compressed += (cnt >=2)? cnt + prev : prev;
					sub = "";
					for(int k=j; k<j+step; k++) {
						if(k<s.length()) sub += s.charAt(k);
					}
					prev = sub; // 다시 상태 초기화
					cnt = 1;
				}
			}
			// 남아있는 문자열에 대해서 처리
			compressed += (cnt >= 2)? cnt + prev : prev;
			// 만들어지는 압축 문자열이 가장 짧은 것이 정답
			answer = Math.min(answer,  compressed.length());
		}
		return answer;
		
	}
	
	public static int mySolution(String s) {
        int answer = (int)1e9;
        if (s.length()==1) return 1;
        for(int step=1; step<=s.length()/2; step++) { // step은 자르는 글자 수 의미
        	ArrayList<String> subs = new ArrayList<>();
        	String compressed = "";
        	int cnt = 1;
        	int idx_limit = (s.length()%step == 0)? s.length() : s.length()+1;
        	
        	// step만큼 문자열을 나눈다. 
        	for(int j=0; j<idx_limit; j+=step) {
        		if( j+step >= s.length()) subs.add(s.substring(j, s.length()));
        		else subs.add(s.substring(j, j+step));
        	}
        	// 나눈 문자열들을 비교 
        	for(int k=0; k<subs.size()-1; k++) {
        		if(subs.get(k).equals(subs.get(k+1))) cnt += 1;
        		else {
        			compressed += (cnt>1)? cnt + subs.get(k) : subs.get(k);
        			cnt = 1;
        		}
        	}
        	
        	// 남아있는 문자열 처리
        	compressed += (cnt>1)? cnt + subs.get(subs.size()-1) : subs.get(subs.size()-1);
        	answer = Math.min(answer, compressed.length());
        }
        
        return answer;
    }
	
	public static void main(String[] args) {
		
		int ans = mySolution("aaaaaaaa");
		int ans2 = solution("");
		System.out.println(ans);
		
	}

}
