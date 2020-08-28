n, k = map(int, input().split())
ans = 0
coin_val = list()
for _ in range(n) :
  coin_val.append(int(input()))

idx= len(coin_val)-1
while True :
  if k >= coin_val[idx] :
    ans += k//coin_val[idx]
    k = k%coin_val[idx]
  else :
    idx -= 1
  if k <= 0:
    break

print(ans)
