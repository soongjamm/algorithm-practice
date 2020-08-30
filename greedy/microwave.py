t = int(input())

time = [500, 60, 10]
ans = ''

for sec in time :
  ans += str(t//sec) + ' '
  t -= sec*(t//sec)
if t != 0 :
  ans = -1

print(ans)