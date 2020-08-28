
## 1
n, k = map(int, input().split())
answer = 0

while n != 1 :
  if n%k == 0:
    n/=k
  else :
    n-=1
  answer+=1
print(answer)

# ## 2
# n, k = map(int, input().split())
# answer = 0

# while n >= k :
#   while n%k != 0:
#     n -= 1
#     answer += 1
#   n //= k
#   answer += 1

# # 나눈 몫이 k보다 작아졌을 경우
# while n > 1 :
#   n -= 1
#   answer += 1

# print(answer)

# ## 3
# n, k = map(int, input().split())
# answer = 0

# while True:
#   target = (n//k)*k # k로 나누고 곱하는 이유 : 나누어 떨어지는 수 만들기 위함
#   answer += (n-target)
#   n = target
#   if n < k:
#     break
#   answer += 1
#   n /= k

# answer += (n-1)
# answer = int(answer)
# print(answer)