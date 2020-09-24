# 볼링공 고르기
# python greedy/bowling_ball.py

# 교재
# 무게가 낮은 공부터 높은 공 순서대로 확인하다 보면 B가 선택하는 경우의 수가 줄어든다
# 이미 계산한 조합은 제외하기 때문이다.

# 입력
# 5 3
# 1 3 2 3 2
# 출력
# 8

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11 

for x in data:
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
  n -= array[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n

print(result)

# # 내 아이디어
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# from itertools import combinations
# import math
# li = list(combinations(arr, 2))
# dup = 0
# for i in li:
#   if i[0] == i[1]:
#     dup += 1

# ans = math.factorial(n)//(math.factorial(n-2)*2) - dup
# print(ans)