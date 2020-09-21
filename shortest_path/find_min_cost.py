# 백준 1916 - 최소비용 구하기
# python shortest_path/find_min_cost.py
## 입력
# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5
## 출력
# 4

import heapq
import sys

input = sys.stdin.readline
# 도시의 개수 n
n = int(input())
# 버스의 개수 m
m = int(input())

INF = 1e9
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF]* (n+1)

for _ in range(m):
  # x에서 y로 가는 비용 z
  x, y, z = map(int, input().split())
  graph[x].append((y,z))

# 출발점 start, 도착점 dest
start, dest = map(int, input().split())

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    # 힙큐에서 가장 비용이 적은 노드 pop
    dist, now = heapq.heappop(q)
    # 이미 처리된 곳이라면 무시
    if distance[now] < dist:
      continue
    # 현재 방문 노드에서 갈 수 있는 모든 노드 방문
    for i in graph[now]:
      cost = distance[now] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 출력
print(distance[dest])


