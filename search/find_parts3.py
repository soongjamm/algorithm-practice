# set() 함수를 이용

#가게의 부품 개수 NotImplementedError
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))
# 손님이 확인 요청한 부품 개수 m
m = int(input())
# 손님이 확인 요청한 전체 부품 번호 x
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')

print()