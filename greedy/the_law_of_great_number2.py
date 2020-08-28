n, m, k = map(int(), input().split())
li = list(map(int(), input().split()))

li.sort(reverse=True)
first = li[0]
second = li[1]

##필요한 가장 큰수의 개수를 계산하는 방법
first_count = int(m/(k+1)) * k
first_count += m%(k+1)

answer = first_count*first + (m-first_count)*second

##연속되는 블록 단위로 계산하는 방법
# answer += (m//(k+1)) * (k*first+second)
# m%=(k+1)
# answer += m*first

print(answer)