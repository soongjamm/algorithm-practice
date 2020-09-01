dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 'area' 값 - 빈칸 : 0, 벽 : 1, 청소됌 : 2
n, m = map(int, input().split())
x, y, d = map(int, input().split())
area = list()

# N*M 영역 영역
for i in range(n) :
  area.append(list(map(int, input().split())))

def turn_left() :
  global d
  d -= 1
  if d == -1 :
    d = 3

ans = 0
turn_cnt = 0

while True :
  if area[x][y] == 0 :
    area[x][y] = 2
    ans += 1
  turn_left()
  turn_cnt += 1
  nx = x + dx[d]
  ny = y + dy[d]

  # 다음 칸이 빈칸이면 이동 후 처음으로
  if area[nx][ny] == 0:
    x, y = nx, ny
    turn_cnt = 0
    continue

  else :
    if turn_cnt != 4 :
      continue
    else :
      nx = x - dx[d]
      ny = y - dy[d]
      # 뒤가 벽인 경우 종료, 아닌 경우 뒤로 이동
      if area[nx][ny] == 1 :
        break
      elif area[nx][ny] == 2 :
        x, y = nx, ny
        turn_cnt = 0
        continue
    
print(ans)
