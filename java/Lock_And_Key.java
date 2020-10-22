
public class Lock_And_Key {
	
	public static int[][] rotate(int[][] key) {
		int[][] new_key = new int[key.length][key.length];
		for(int i=0; i<key.length; i++) {
			for(int j=0; j<key.length; j++) {
				new_key[key.length-1-j][i] = key[i][j];
			}
		}
		
		return new_key;
	}
	
	public static boolean check(int[][] new_lock, int lock_size, int key_size) {
		for(int i=0; i<lock_size; i++) {
			for(int j=0; j<lock_size; j++) {
				if(new_lock[i+key_size][j+key_size] != 1) 
					return false ;
			}
		}
		return true;
	}
    
	public static boolean mySolution(int[][] key, int[][] lock) {
        int size_mn = key.length*2+lock.length;
        int[][] new_lock = new int[size_mn][size_mn];
        for(int i=0; i<lock.length; i++) {
        	for(int j=0; j<lock.length; j++) {
        		new_lock[key.length+i][key.length+j] = lock[i][j];
        	}
        }
        
        for(int i=0; i<size_mn-key.length; i++) {
        	for(int j=0; j<size_mn-key.length; j++) {
        		for(int k=0; k<4; k++) {

        			// 키 꽂기
        			for(int a=0; a<key.length; a++) {
        				for(int b=0; b<key.length; b++) {
        					new_lock[i+a][j+b] += key[a][b];
        				}
        			}
        			
        			boolean res = check(new_lock, lock.length, key.length);
        			if (res) return true;
        			
        			// 키 빼
        			for(int a=0; a<key.length; a++) {
        				for(int b=0; b<key.length; b++) {
        					new_lock[i+a][j+b] -= key[a][b];
        				}
        			}
        			
        			key = rotate(key);
        		}
        	}
        }
        
        return false;
    }
    
	public static void main(String[] args) {
		int[][] key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
		int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
		boolean ans = mySolution( key, lock ); // true
		System.out.println(ans);
	}

}
