n, m, k = map(int, input().split())
li = list(map(int, input().split()))
answer = 0

li.sort(reverse=True)
first = li[0]
second = li[1]
c = k
for _ in range(m):
  if c > 0 :
    answer += first
    c-=1
  else :
    answer += second
    c = k 
  print(answer)

print(answer)

