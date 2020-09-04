import collections

n = int(input())
k = int(input())
m = [[0]*n for _ in range(n)]
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
rotate = [list(input().split()) for _ in range(l)] 

snake = collections.deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1

# 지도에 사과 표시 
# 0 = 빈 칸, 1 = 사과가 있는 칸, 2 = 이동한 칸
for i in apple :
  m[i[0]-1][i[1]-1] = 1

time = 0
snake.append([0,0])

rotate.reverse()
rtt = list()
if rotate :
  rtt = rotate.pop()

def turn_left() :
  global d
  d = (d-1)%4

def turn_right() :
  global d
  d = (d+1)%4

while True :
  time += 1
  [x, y] = snake[len(snake)-1]
  nx = x + dx[d]
  ny = y + dy[d]

  # 머리 이동
  ## 범위를 벗어나거나, 자기 몸에 부딪힐 경우 종료
  ## 다음 위치를 snake의 오른쪽에 추가한다.
  if not 0 <= nx < n or not 0 <= ny < n :
    break
  if [nx,ny] in snake :
    break
  snake.append([nx,ny])
  
  # 꼬리 이동
  ## 사과가 없을 때. 왼쪽을 pop
  ## 사과가 있을 때. 그대로 유지
  if m[nx][ny] != 1 : 
    if snake :
      t = snake.popleft()
      m[t[0]][t[1]] = 0 #test

  m[nx][ny] = 2 # test
  if rtt[0] == str(time) :
    if rtt[1] == 'L' :
      turn_left()
    elif rtt[1] == 'D' :
      turn_right()
    if rotate :
      rtt = rotate.pop()
  x, y = nx, ny
  # for i in m :
  #   print(i)
  # print('snake(time %d)\n', time, snake)


  


print(time)