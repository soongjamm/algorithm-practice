# 백준 11404 플로이드
# python shortest_path/floyd.py

import sys
input = sys.stdin.readline

INF = 1e9
# 도시의 개수 n
n = int(input())
# 버스의 개수 m
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]
# 버스의 정보 입력
for i in range(m):
  # 출발 도시 a, 도착 도시 b, 이동 비용 c
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b],c)
  
# 자기 자신으로 가는 노선은 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j:
      graph[i][j] = 0

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=' ')
    else:
      print(graph[a][b], end=' ')
  print()