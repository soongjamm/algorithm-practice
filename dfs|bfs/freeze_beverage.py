# from collections import deque

# DFS 사용
n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 2차원 리스트의 맵 정보 입력
graph = []
for i in range(n) :
  graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) :
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<= -1 or x>= n or y<= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0 :
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치도 모두 제귀적으로 호출
    for i in range(4) :
      nx, ny = x+dx[i], y+dy[i]
      dfs(nx, ny)
    return True
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n) :
  for j in range(m) :
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True :
      result += 1

print(result)

## BFS 사용 
# n, m = map(int, input().split())
# frame = [list(input()) for _ in range(n)]
# visited = [ [False] *m  for _ in range(n)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# ans = 0

# def bfs(frame, start) :
#   global visited
#   q = deque()
#   q.append(start)
  
#   while q :
#     pos = q.popleft()
#     x, y = pos[0], pos[1]
#     for i in range(4) :
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < n and 0 <= ny < m and frame[nx][ny] == '0':
#         if visited[nx][ny] == False :
#           visited[nx][ny] = True
#           q.append([nx,ny])

# for i in range(n) :
#   for j in range(m) :
#     if visited[i][j] == False and frame[i][j] == '0' :
#       visited[i][j] = True
#       bfs(frame, [i,j])
#       ans += 1
  
# print(ans)



