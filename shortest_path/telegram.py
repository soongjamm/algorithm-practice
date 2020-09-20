# 전보
# python shortest_path/telegram.py
## 입력
# 3 2 1 
# 1 2 4
# 1 3 2
## 출력
# 2 4
import heapq
import sys

inpurt = sys.stdin.readline
INF = int(1e9)
# 도시 개수 n , 통로 개수 m, 메세지를 보내고자 하는 도시 c
n, m, c = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for i in range(1, m+1):
  x, y, z = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 z
  graph[x].append((y,z))

def djikstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

djikstra(c)

# 도달할 수 있는 노드의 개수
count = -1
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_dist = 0
for d in distance:
  # 도달할 수 있는 노드인 경우
  if d != INF:
    count += 1
    max_dist = max(d, max_dist)

print(count, max_dist)