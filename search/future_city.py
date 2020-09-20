# 미래 도시
# python search/future_city.py
## 입력
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
## 출력
# 3

INF = 1e9

# 전체 회사의 개수 n, 경로의 개수 m
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자신-자신 경로를 0 으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 초기화
for i in range(m):
  # a와 b 서로 가는 시간 1
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# k번 - x번 회사 순으로 방문
x, k = map(int, input().split())

for i in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])
print(graph)

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]
# 도달할 수 없는 경우, -1 출력
if distance >= INF:
  print("-1")
else:
  print(distance)