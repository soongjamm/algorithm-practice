# 금광

t = int(input())

# 테스트케이스 만큼 진행
for _ in range(t):
  # 입력 받기
  n, m = map(int, input().split())
  data = [[0]*(m+2) for _ in range(n+2)]
  tmp = list(map(int, input().split()))
  tmp.reverse()
  for i in range(1, n+1):
    for j in range(1, m+1):
      data[i][j] = tmp.pop()
  
  res = 0
  d = [[0]*(m+2) for _ in range(n+2)]
  for i in range(1, n+1):
    d[i][1] = data[i][1]

  for j in range(1, m+1):
    for i in range(1, n+1):
      t = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + data[i][j]
      d[i][j] = max(t, d[i][j])
      if d[i][j] > res:
        res = d[i][j]

    for i in range(1, n+1):
      print(d[i])
    print(res)

# input 
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# output
# 19
# 16