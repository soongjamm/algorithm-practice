# 도시 분할 계획. 2개의 신장트리로 분할
# 1개의 신장트리에서, 마지막으로 더해준 (더해준 것중 가장 비용이 큰) 것을 다시 빼준다. 
# python graph/urban_division_plan.py
## 입력
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
## 출력
# 8

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 집의 개수 n, 길의 개수 m
n, m = map(int, input().split())

# 부모 테이블
parent = [0] * (n+1)
for i in range(n):
  parent[i] = i
# 경로 저장
edges = []

# 경로 정보 입력
for i in range(m):
  # a번과 b번 집을 연결하는 유지비 c
  a, b, c = map(int, input().split())
  edges.append((c,a,b))

edges.sort()
result = 0
last = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost


print(result-last)