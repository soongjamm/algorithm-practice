# 곱하기 혹은 더하기
# python greedy/multiply_or_plus.py

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수중에서 하나라도 '0' 혹은 '1'인 경우, 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)

# total = 0
# s = list(map(int,input()))

# # plus = 0, multiply = 1

# sign = 0
# for i in s:
#   if sign == 0:
#     total += i
#   elif sign == 1:
#     total *= i
  
#   if i == 0 or i == 1:
#     sign = 0
#   else:
#     sign = 1
  
#   print(i)

# print(total)