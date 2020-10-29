import java.util.ArrayList;

public class Column_Beam {

	public static int[][] cols;
	public static int[][] beams;
	
	
	
	
	public static int[][] solution(int n, int[][] build_frame) {
		ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>();
        
		// 최대 작업 개수 1000개 
        for(int i=0; i<build_frame.length; i++) {
        	
        	int x = build_frame[i][0];
        	int y = build_frame[i][1];
        	int stuff = build_frame[i][2]; // 설치 또는 삭제할 구조물의 종류 기둥(0), 보(1)
        	int operate = build_frame[i][3]; // 구조물의 설치(1)-삭제(0)
        	
        	if( operate == 0 ) { // 삭제하는 경
        		// 우선 삭제 해본다.
        		int index = 0;
        		for(int j=0; j<answer.size(); j++) {
        			if(x == answer.get(j).get(0) && y == answer.get(j).get(1) && stuff == answer.get(j).get(2)) {
        				index = j;
        			}
        		}
        		ArrayList<Integer> erased = answer.get(index);
        		answer.remove(index);
        		if(!possible(answer)) { // 가능한 구조물인지 확인 
        			answer.add(erased); // 가능한 구조물이 아니라면 다시 설치 
        		}
        	
        	if( operate == 1 ) {
        		// 일단 설치를 해본다. 
        		ArrayList<Integer> inserted = new ArrayList<Integer>();
        		inserted.add(x);
        		inserted.add(y);
        		inserted.add(stuff);
        		answer.add(inserted);
        		if(!possible(answer) ) {
        			answer.remove(answer.size() - 1);
        		}
        	}
        	
        
        
        	
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] arr = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
		System.out.println(solution(5, arr));
	}

}
