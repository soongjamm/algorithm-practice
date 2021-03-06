# 자물쇠와 열쇠

# 내 아이디어 :
# key와 lock을 xor해서 lock의 원소 전부가 1이 되면 True
# key를 회전시켜 나오는 4가지 방향을 모두 고려
# key를 이동시킬 때, 한 칸만 lock에 걸치는 경우도 고려했다.
# 이 때, lock의 시작점을 0-(key길이인 m -1)부터 n까지 검사했다.

import copy

def check(i, j, key, lock):
  m = len(key)
  n = len(lock)

  # 확인차. key 출력
  # # print(i, j)
  # for a in range(m):
  #   print(key[a], ' -- in check')

  new_lock = copy.deepcopy(lock)
  for a in range(m):
    for b in range(m):
      if 0 <= a+i < n and 0 <= b+j < n:
        if not(key[a][b] ^ lock[a+i][b+j] == 1):
          return
        new_lock[a+i][b+j] = 1
  
  
  for a in range(n):
    for b in range(n):
      if new_lock[a][b] == 0:
        return
  
  # for k in range(n):
  #   print(lock[k], ' - lock')
  # for k in range(m):
    # print(key[k], ' - key', i, j)
  
  return True

def turn_right(key):
  m = len(key)-1
  new_key = [[0]*len(key) for _ in range(len(key))]
  for i in range(m+1):
    for j in range(m+1):
      new_key[i][j] = key[m-j][i] 
  
  return new_key

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    for i in range(0-(m-1), n):
      for j in range(0-(m-1), n):
        for k in range(4):
          res = check(i, j, key, lock)
          if res == None:
            key = turn_right(key)
            # print(key[0], ' - in solution')
          elif True:
            # print(True)
            return True
    
    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) # True