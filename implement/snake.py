# 뱀
## 입력
# 6 
# 3
# 3 4
# 2 5
# 5 3
# 3 
# 3 D
# 15 L
# 17 D
## 출력
# 9

# 0은 빈 칸, 1은 사과 위치

from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * (n) for _ in range(n)] # 게임 보드
for _ in range(k): # 사과 위치 입력
  x, y = map(int, input().split())
  board[x-1][y-1] = 1
l = int(input()) # 뱀의 방향 변환 횟수
rotation = deque()
for _ in range(l): # 뱀의 방향 변환 정보 입력
  x, c = input().split()
  rotation.append((int(x), c))

# 동남서북 순서. 오른쪽은 +1, 왼쪽은 -1
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

# 최초 뱀 위치 설정
snake = deque()
snake.append((0,0)) 
face = 0 # 최초에 동쪽 바라보는 중
time = 0

while True:
  time += 1
  x, y = snake[0]
  nx = x+dx[face]
  ny = y+dy[face]

  # 방향 전환 여부 확인
  if rotation and rotation[0][0] == time:
    rotate = rotation.popleft()
    # print(rotate)
    if rotate[1] == 'L':
      face = (face-1)%4
    else:
      face = (face+1)%4

  if 0 <= nx < n and 0 <= ny < n:
    # 만약 nx, ny에 사과가 있다면 크기+1
    if (nx,ny) in snake: # nx-ny에 뱀의 몸이 있다면 종료 
      break
    snake.appendleft((nx,ny)) # 머리를 늘린다.
    # print(snake)
    if board[nx][ny] == 1: 
      board[nx][ny] = 0
    else:
      snake.pop() # 사과를 먹은게 아니라면 꼬리를 당긴다.
  else: # 벽에 부딪혔을 때 종료
    break

print(time)

    
    
  

