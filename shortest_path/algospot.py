# 백준 1261 - 알고스팟
# python shortest_path/algospot.py
## 입력
# 3 3
# 011
# 111
# 110
## 출력
# 3

import heapq
import sys

input = sys.stdin.readline
# 미로의 가로크기 m, 세로크기 n
m, n = map(int, input().split())
# 미로의 상태
graph = [list(input().rstrip()) for _ in range(n)]
crush = [[-1]*m for _ in range(n)]

def dijkstra():
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  q = []
  crush[0][0] = 0
  heapq.heappush(q, (0,(0,0)))
  while q:
    cnt, (x, y) = heapq.heappop(q)
    if x == n-1 and y == m-1:
      break
    # 4 방향으로 다 움직여 본다
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<n and 0<=ny<m and crush[nx][ny] < 0:
        crush[nx][ny] = cnt
        if graph[nx][ny] == '1':
          heapq.heappush(q, (cnt+1, (nx,ny)))
        else:
          heapq.heappush(q, (cnt, (nx,ny)))
        
    

dijkstra()
print(crush[n-1][m-1])
