n, m = map(int, input().split())
p = [list(map(int,list(input()))) for _ in range(n)]
p2 = [list(map(int, list(input()))) for _ in range(n)]

# 시작점 i,j부터 3x3 부분행렬 뒤집음
def flip(a, b):
  global p
  for i in range(a, a+3):
    for j in range(b, b+3):
      p[i][j] = 1 - p[i][j]

# 처음 시작점 i, j 설정
cnt = 0

for i in range(n-2):
  for j in range(m-2): 
    if p[i][j] != p2[i][j]: 
      flip(i,j) 
      cnt += 1

if p == p2:
  print(cnt)
else:
  print(-1)