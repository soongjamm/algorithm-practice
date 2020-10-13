
# https://www.acmicpc.net/problem/18428
n = int(input())
hallway = []
for i in range(n):
  hallway.append(list(input().split()))

# 우선 벽을 먼저 세운다.
# 벽을 다 세우면 선생님과 같은 라인에 벽이 있는지, 없다면 학생이 있는지 확인한다.
# 벽을 다 안세웠다면 cnt를 하나씩 증가시키며 벽을 세운다.

def check(arr, x, y):
  # 행 위쪽
  s = False
  for i in range(x, -1, -1):
    if arr[i][y] == 'S':
      s = True
    if arr[i][y] == 'O':
      break
  if s:
    return False
  
  # 행 아래쪽
  s = False
  for i in range(x, n):
    if arr[i][y] == 'S':
      s = True
    if arr[i][y] == 'O':
      break
  if s:
    return False
    
  # 열 왼쪽
  s = False
  for j in range(y, -1, -1):
    if arr[x][j] == 'S':
      s = True
    if arr[x][j] == 'O':
      break
  if s:
    return False

  # 열 오른쪽
  s = False
  for j in range(y, n):
    if arr[x][j] == 'S':
      s = True
    if arr[x][j] == 'O':
      break
  if s:
    return False
  
  return True

flg = False
def dfs(cnt):
  global hallway, flg
  if flg:
    return 
  if cnt == 3:
    tmp_flg = True
    for i in range(n):
      for j in range(n):
        if hallway[i][j] == 'T':
          if check(hallway, i, j):
            tmp_flg = True
          else:
            return
    if tmp_flg:
      flg = True
    
  else:
    for i in range(n):
      for j in range(n):
        if hallway[i][j] == 'X':
          hallway[i][j] = 'O'
          dfs(cnt+1)
          hallway[i][j] = 'X'
    

dfs(0)

if flg:
  print('YES')
else:
  print("NO")