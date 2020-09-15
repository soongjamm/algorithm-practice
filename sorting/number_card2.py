# 백준 10816
# python sorting/number_card2.py
## 입력
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
## 출력
# 3 0 0 1 2 0 0 2

# 처음엔 binary search로 풀려고 했다가 시간초과가 계속 났음
# target이 여러개 일땐 binary search보다 딕셔너리로 계수정렬(?) 하는게 낫다.
import sys
input = sys.stdin.readline
n = int(input())
na = list(map(int, input().split()))
m = int(input())
ma = list(map(int, input().split()))

di = dict()

for i in na:
  try:
    di[i] += 1
  except:
    di[i] = 1

for i in ma:
  try:
    print(di[i], end = ' ')
  except:
    print(0, end=' ')
