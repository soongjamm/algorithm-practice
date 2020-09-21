# 백준 1753
# python shortest_path/shortest_path.py
## 입력
# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
## 출력
# 0
# 2
# 3
# 7
# INF
import heapq
import sys

input = sys.stdin.readline
INF = 1e9
# 정점의 개수 V, 간선의 개수 e
V, e = map(int, input().split())
# 시작 정점의 번호 k
k = int(input())

graph = [[] * (V+1) for _ in range(V+1)]
dist = [INF] * (V+1)

# e개의 줄에 걸쳐 각 간선을 나타내는 세개의 정수 u,v,w 입력 받음
for _ in range(e):
  # u에서 v로 가는 가중치 w인 간선
  u, v, w = map(int, input().split())
  graph[u].append((v,w))

def dijkstra(start):
  q = []
  dist[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    distance, now = heapq.heappop(q)
    # 이미 처리된 적이 있는 노드라면 무시. 
    # (pop해서 나온 비용이 최단거리 테이블보다 클 때)
    if dist[now] < distance:
      continue
    # 현재 노드에서 갈 수 있는 모든 노드를 검사
    for i in graph[now]:
      cost = dist[now] + i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(k)
# dist 출력
for a in range(1, V+1):
  if dist[a] == INF:
    print("INF")
  else:
    print(dist[a])


