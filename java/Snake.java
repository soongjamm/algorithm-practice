import java.util.*;


class Pos {
	private int x;
	private int y;
	
	Pos(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
}

class Order {

	private int time;
	private char dir;
	
	Order(int time, char dir) {
		this.time = time;
		this.dir = dir;
	}
	
	public int getTime() {
		return time;
	}
	
	public char getDir() {
		return dir;
	}
}

public class Snake {
	// 동-남-서-북 순서
	public static int[] dx = {0, 1, 0, -1};
	public static int[] dy = {1, 0, -1, 0};
	
	public static Queue<Order> order = new LinkedList<>(); // 회전 정보
	public static Deque<Pos> body = new ArrayDeque<>();
	public static int[][] apple; // 사과 위치 저장
	
	public static int N, K, L;
	
	public static int turn(int dir, char c) {
		if (c == 'L') dir = (dir == 0)? 3 : dir - 1;
		else dir = (dir + 1) % 4;
		return dir;
	}
	
	public static int solution() {
		Order nextOrder;
		int time = 0;
		int face = 0; // 오른쪽 +1, 왼쪽 -1 
		
		// 시작점
		body.add(new Pos(1,1)); 
		nextOrder = order.poll();
		
		while(true) {
			Pos head = body.peek();
			int nx = head.getX() + dx[face];
			int ny = head.getY() + dy[face];
			time += 1;
			
			// 맵을 벗어나면 게임이 끝
			if( !(1 <= nx && nx <= N && 1 <= ny && ny <= N)) {
				break;
			}
			// 자기 자신과 부딪혀도 게임이 끝
			boolean end = false;
			for(Pos p : body) {
				if (p.getX() == nx && p.getY() == ny) {
					end = true;
					break;
				}
			}
			if(end) break;
			
			// 사과가 있는 자리인지 검사
			// 사과가 있는 자리면 길이가 늘어난다.
			body.addFirst(new Pos(nx, ny));
			if(apple[nx][ny] == 1) {
				apple[nx][ny] = 0;
			}
			else body.pollLast();
			
			if(nextOrder.getTime() == time) {
				
				face = turn(face, nextOrder.getDir());
				if(!order.isEmpty()) {
					nextOrder = order.poll();
				}
				
			}
			
		}
		
		return time;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		// 기본 입력 
		N = sc.nextInt();
		K = sc.nextInt();
		apple = new int[N+1][N+1];
		for(int i=0; i<K; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			apple[x][y] = 1;
		}
		L = sc.nextInt();
		for(int i=0; i<L; i++) {
			int sec = sc.nextInt();
			char dir = sc.next().charAt(0);
			order.add(new Order(sec, dir));
		}
		
		System.out.println(solution());
		
		
		
	}

}
