# 경쟁적 전염

from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, a, b = map(int, input().split())

# 인덱스가 0부터 시작하므로
a -= 1
b -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while q:
    now = q.popleft()
    x, y, t = now[0], now[1], now[2]
    if t == s:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if  data[nx][ny] == 0:
          data[nx][ny] = data[x][y]
          q.append((nx,ny, t+1))



q = deque()
for i in range(n):
  for j in range(n):
    if data[i][j] != 0:
      q.append((i,j,0,data[i][j]))

q = deque(sorted(q, key = lambda x: x[3]))
if s > 0:
  bfs()
print(data[a][b])
    

