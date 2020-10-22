# 숨바꼭질
# 모든 거리가 1이기 때문에 BFS를 이용해서 풀 수도 있다.

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = int(1e9)
distance = [INF] * (n)
for i in range(m):
  a, b = map(int, input().split())
  a-=1
  b-=1
  graph[a].append(b)
  graph[b].append(a)

q = []
start = 0
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for node in graph[now]:
    cost = dist + 1
    if cost < distance[node]:
      distance[node] = cost
      heapq.heappush(q, (cost, node))

max_value = max(distance)
barn = distance.index(max_value)
count = distance.count(max_value)
print(barn+1, max_value, count)
  
# 입력
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
# 출력
# 4 2 3