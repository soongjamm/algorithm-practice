# 최대한 +를 한 다음 -를 하면 된다.

# -를 기준으로 값 저장
# ['4+3+2', '5+6+7'] 처럼 저장된다.
example = input().split('-') 
result = 0

# 첫번째 인덱스(['4+3+2'])값을 result에 더한다.
for i in example[0].split('+') : 
  result += int(i)  
  print(i)

# 나머지 인덱스를 돌면서 값을 result에서 빼준다.
for i in example[1:] : 
  for j in i.split('+'): 
      result -= int(j) 

print(result)


