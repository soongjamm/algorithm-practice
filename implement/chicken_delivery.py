# 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
arr = []
house = []
chicken = []

for i in range(n):
  arr.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      house.append((i,j))
    if arr[i][j] == 2:
      chicken.append((i,j))

# m개의 가능한 치킨집 조합 뽑아내기
chickenList = list(combinations(chicken, m)) # m개의 좌표의 모든 경우의 수

# chic = m개의 좌표 
# 어느 chic 이 최선인지 계산해야 한다. 
answer = int(1e9)
for chic in chickenList: 
  result = 0
  # 한 집에 대해 어떤 치킨집이 제일 가까운지 치킨 거리를 구한다.
  # 치킨집은 m개의 치킨집에 한정됌
  for hx, hy in house:
    temp = int(1e9)
    for cx, cy in chic:
      temp = min(temp, abs(hx-cx) + abs(hy-cy)) # 
    # 가장 가까운 치킨집까지의 거리를 더함
    result += temp
  answer = min(answer, result)

print(answer)
