# 곱하기 혹은 더하기
# python greedy/multiply_or_plus.py

total = 0
s = list(map(int,input()))

# plus = 0, multiply = 1

sign = 0
for i in s:
  if sign == 0:
    total += i
  elif sign == 1:
    total *= i
  
  if i == 0 or i == 1:
    sign = 0
  else:
    sign = 1
  
  print(i)

print(total)