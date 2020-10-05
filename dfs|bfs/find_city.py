# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# 모든 노드까지의 거리를 구하기 위해 BFS를 이용할 것
from collections import deque
import sys
# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x
n, m, k, x = map(int, sys.stdin.readline().split())
# m개의 줄 만큼 A->B 단방향 도로 정보 주어짐
road = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  road[a].append(b)
dist = [-1] * (n+1)

def bfs():
  q = deque()
  q.append(x)
  dist[x] = 0
  while q:
    pos = q.popleft()
    for np in road[pos]:
      if dist[np] == -1: 
        dist[np] = dist[pos] + 1
        q.append(np)

# 답 출력
answer = False
bfs()
for i in range(1, n+1):
  if k == dist[i]:
    print(i)
    answer = True

if answer == False:
  print(-1)