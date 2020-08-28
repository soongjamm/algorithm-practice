n = int(input())
answer = -1 # 조건문을 만족하지 못하면 그대로 -1
dic = {3, 6, 9, 12} # 3으로만 나누어지는 수

cnt = 0

# 5의 배수인 경우
if n % 5 == 0 :
  answer = n//5
else :  
  if n in dic :
    answer = n // 3
  else :
    # 5의 배수와 3의 배수가 더해진 경우
    # (계속해서 5kg 봉지에 담다가 남은 설탕이 3kg 으로만 나눠질 때 모두 3kg 봉지에 담는다.)
    ## 3으로만 나눠지는 수가 나올 때 까지 반복해서 5를 빼준다. 
    ## 5를 빼줄 때 마다 카운트 해준다. (5kg 봉지 카운트)
    while n >= 3 :
        n -= 5
        cnt += 1
        if n in dic :
          cnt += n//3
          answer = cnt
          break

print(answer)