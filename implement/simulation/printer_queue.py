from collections import deque

t = int(input())

for i in range(t) :
  n, m = map(int, input().split())
  pri = input()
  dq = deque()
  for j in range(len(pri)):
    if pri[j] == ' ':
      continue
    dq.append(pri[j])
  cnt = 0 
  while True :
    poped = dq.popleft()
    m -= 1
    if not dq or poped >= max(dq) :
      cnt += 1
      if m == -1 :
        print(cnt)
        break
    else :
      dq.append(poped)
      if m == -1 :
        m = len(dq)-1
  