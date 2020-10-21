# 성적 비교
# A에서 B나 B에서 A로 도달이 가능하면 성적 비교가 가능하다. 
# (A와 B가 비교 가능하다는 뜻 이므로)

INF = int(1e9)

n, m = map(int, input().split())
data = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      data[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  data[a][b] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      data[a][b] = min(data[a][b], data[a][k] + data[k][b])

result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if data[i][j] != INF or data[j][i] != INF:
      count += 1
  if count == n:
    result += 1
print(result)
