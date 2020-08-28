coin_li = [500, 100, 50, 10, 5, 1]
count = 0
tmp = 0

pay = int(input())
remain = 1000-pay

for coin in coin_li:
  if remain >= coin:
    count += remain//coin
    remain %= coin
  
print(count)


