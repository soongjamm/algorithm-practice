# 백준 1389 케빈 베이컨의 6단계 법칙
# python shortest_path/kevin_bacon.py


INF = 1e9
# 유저의 수 n, 친구 관계의 수 m
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)] 
ans = [0]*(n+1)
# a와 b가 친구면, b와 a도 친구다.
# 값은 a와 b가 몇 단계를 거쳐 친구인지를 나타냄
for a in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      if graph[a][k]+graph[k][b] >= 2:
        graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

ans[0]=INF
for i in range(1,n+1):
  for j in graph[i]:
    if j!=INF:
      ans[i] += j

print(ans.index(min(ans)))