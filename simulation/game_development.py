n, m = map(int, input().split())
x, y, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_map = list()

for i in range(n):
  game_map.append(list(map(int,input().split())))

def turn_left() :
  global d
  d = (d-1) if d != 0 else 3
  
res = 1
i = 0
while i < 4:
  turn_left()
  nx = x + dx[d]
  ny = x + dy[d]
  if 0 <= nx < n and 0 <= ny < m and game_map[nx][ny] == 0 :
    game_map[nx][ny] = 2
    x, y = nx, ny
    i = 0
    res += 1
    continue
  else :
    i += 1
    if i == 4 :
      nx = x - dx[d]
      ny = y - dy[d]
      if game_map[nx][ny] != 1 :
        x, y = nx, ny
        res += 1
      else :
        break


print(res)
