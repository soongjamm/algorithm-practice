# 공백을 기준으로 구분하여 데이터 입력

## split() - 공백을 기준으로 나누어 리스트로 만듦
## map - 해당 리스트의 모든 원소에 int() 함수 적용
data = list(map(int, input().split()))
print(data)

## 입력 데이터가 적을 때
n, m, k = map(int, input().split())
print(n, m, k)
