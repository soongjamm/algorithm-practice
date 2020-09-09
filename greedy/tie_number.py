n = int(input())
li = list()
for _ in range(n):
  li.append(int(input()))
li.sort()

ans = 0

# 음수~0 계산
while li and li[0] < 1:
  if len(li) > 1 and li[1] < 1:
    ans += li[0] * li[1]
    li = li[2:]
  else:
    ans += li[0]
    li = li[1:]

# 양수 계산
while len(li) > 1:
  if li[-1] == 1 or li[-2] == 1:
    li.remove(1)
    ans += 1
    continue
  else:
    ans += li[-1] *. li[-2]
    li = li[:-2]

if li:
  ans += li[0]

print(ans)
  

