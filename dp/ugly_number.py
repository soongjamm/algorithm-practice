# 못생긴 수

# 못생긴 수란 2, 3, 5 만을 소인수로 가지는 수
# n번째 못생긴 수를 구하라

n = int(input())
ugly = [0]*n # 못생긴 수를 담을 DP 테이블
ugly[0] = 1

# 2배, 3배, 5배를 위한 인덱스
# 2, 3, 5 각 수에 대해서 몇번째 인덱스까지 처리했는지 기억하기 위함
i2 = i3 = i5 = 0
# 처음에 사용할 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
  # 가능한 곱셈 결과 중 가장 작은 수를 선택
  ugly[l] = min(next2, next3, next5)
  # 인덱스에 따라서 곱셈 결과를 증가
  # ugly[i]에 가장 작은 결과값을 넣어줬으니, 가장 작은 결과값이 들어있던 변수에 새로운 수를 곱해준다.
  if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])
