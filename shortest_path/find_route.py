# 백준 11403 경로찾기
# python shortest_path/find_route.py
## 입력
# 3
# 0 1 0
# 0 0 1
# 1 0 0
## 출력
# 1 1 1
# 1 1 1
# 1 1 1

# 플로이드 워셜 변형

# 정점의 개수 n
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# k번 노드를 거쳐가는 경우를 탐색
for k in range(n):
  for a in range(n):
    for b in range(n):
      if graph[a][k] + graph[k][b] == 2:
        graph[a][b] = 1

for a in range(n):
  for b in range(n):
    print(graph[a][b], end = ' ')
  print()

