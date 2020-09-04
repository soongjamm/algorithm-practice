from collections import deque
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
visited = [ [False]*m for _ in range(n) ]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs() :
  global maze, visited
  d = [[0]*m for _ in range(n)]
  d[0][0] = 1
  visited[0][0] = True
  q = deque()
  q.append([0,0])
  cnt=0
  while q :
    cnt+=1
    pos = q.popleft()
    x, y = pos[0], pos[1]
    for i in range(4) :
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1':
        if visited[nx][ny] == False :
          q.append([nx, ny])
          visited[nx][ny] = True
          d[nx][ny] = d[x][y] + 1
          if nx == n-1 and ny == m-1 :
            break

  return d[n-1][m-1]




print(bfs())
