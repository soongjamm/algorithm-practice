# 화성 탐사
# 다익스트라 (2차원 배열을 사용하면 노드가 10000개 이상이여서 플로이드 워셜은 부적합)
import heapq

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# test case 수 
t = int(input())
for _ in range(t):
  # 탐사 공간의 크기 n
  n = int(input())
  graph = []
  INF = int(1e9)
  distance = [[INF] * n for _ in range(n)]
  # 각 칸의 비용 입력
  for i in range(n):
    graph.append(list(map(int, input().split())))
  
  q = []
  heapq.heappush(q, ( graph[0][0], (0,0) )) # 시작 지점
  distance[0][0] = graph[0][0]

  while q:
    dist, now = heapq.heappop(q)
    if distance[now[0]][now[1]] < dist:
      continue
    for i in range(4):
      nx, ny = now[0] + dx[i], now[1] + dy[i]
      if 0 <= nx < n and 0<= ny < n:
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, (nx, ny)) )

  print(distance[n-1][n-1])

# 입력
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 출력
# 20
# 19
# 36