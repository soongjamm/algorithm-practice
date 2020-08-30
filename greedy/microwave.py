t = int(input())

time = [300, 60, 10]
ans = ''

for sec in time :
  ans += str(t//sec) + ' '
  t -= sec*(t//sec)
if t != 0 :
  ans = str(-1)

print(ans)

# t = int(input())

# if t % 10 == 0 :
#   A = B = C =0
#   A = t//300
#   B = (t%300)//60
#   C = (t%300)%60//10
#   print(A, B, C)
# else :
#   print(-1)