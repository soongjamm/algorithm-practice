n = int(input())
lopes = list()
for i in range(n):
  lopes.append(int(input()))
lopes.sort(reverse=True)

cnt = 0
sum = 0
for i in range(n):
  cnt += 1
  tmp = (cnt*lopes[i])
  # sum이 tmp보다 크거나 같으면 추가로 로프를 더하기 전이 더 많은 중량을 든다.
  if sum < tmp:
    sum = tmp

print(sum)




