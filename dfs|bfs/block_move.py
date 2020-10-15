# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def get_next_pos(pos, board):
  next_pos = []
  pos = list(pos)
  pos1, pos2 = pos[0], pos[1]
  x1, y1 = pos1
  x2, y2 = pos2
  
  # 상하좌우
  for i in range(4):
    nx1, ny1 = x1+dx[i], y1+dy[i] 
    nx2, ny2 = x2+dx[i], y2+dy[i]
    if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
      np = { (nx1,ny1), (nx2,ny2) }
      next_pos.append(np)
      # print("candi1", (nx1,ny1), (nx2,ny2))

  # 회전
  # 현재 가로일 때
  if x1 == x2: # 가로일때
    for j in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
      if board[x1+j][y1] == 0 and board[x2+j][y2] == 0: # 위쪽 혹은 아래쪽 두칸이 모두 비어 있다면
        next_pos.append({(x1, y1), (x1+j, y1)})
        next_pos.append({(x2, y2), (x2+j, y2)})
        # print("candi2", {(x1, y1), (x1+j, y1)}, {(x2, y2), (x2+j, y2)})
  elif y1 == y2: # 세로일때
    for j in [-1, 1]: # 왼쪽이나 오른쪽으로 회전
      if board[x1][y1+j] == 0 and board[x2][y2+j] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어있다면
        next_pos.append({(x1, y1), (x1, y1+j)})
        next_pos.append({(x2, y2), (x2, y2+j)})
        # print("candi3", {(x1, y1), (x1+j, y1)}, {(x2, y2), (x2+j, y2)})
       
        # print((x1, y1), (x1, y1+j), (x1, y1), (x1, y1+j))
      
  return next_pos

def solution(board):
    n = len(board)
    visited = []
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
      for j in range(n):
        new_board[i+1][j+1] = board[i][j]
    for i in range(len(new_board)):
      print(new_board[i])
    pos = {(1,1), (1,2)}
    q = deque()
    q.append((pos, 0))
    visited.append(pos)

    while q:
      pos, cost = list(q.popleft())
      if (n, n) in pos:
        return cost
      for next_pos in get_next_pos(pos, new_board):
        if next_pos not in visited:
          visited.append(next_pos)
          q.append((next_pos, cost+1))
      

    return 0


# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))