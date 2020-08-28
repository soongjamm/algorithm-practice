n = int(input())
p = list(map(int, input().split()))
wait = 0
total = 0

for i in range(len(p)):
  min_val = min(p)
  wait += min_val
  total += wait
  p.remove(min_val)
  
print(total)
