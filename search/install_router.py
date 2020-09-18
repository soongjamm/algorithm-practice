# 백준 2110 - 공유기 설치
# python search/install_router.py
## 입력
# 5 3
# 1
# 2
# 8
# 4
# 9
## 출력
# 3

import sys
input = sys.stdin.readline()
#집의 개수 n, 공유기의 개수 c
n, c = map(int, input().split())
house = list()
for _ in range(n):
  house.append(int(input()))

house.sort()

def binary_search(arr, target, start, end):
  res = 0
  while start <= end:
    mid = (start+end) // 2
    cnt = 1
    cur_house = house[0]

    for i in range(1,n):
      if cur_house + mid <= house[i]:
        cnt += 1
        cur_house = house[i]

    if cnt >= target:
      res = mid
      start = mid + 1
    else:
      end = mid - 1
  
  return res


print(binary_search(house, c, 1, house[-1]-house[0]))