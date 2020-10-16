# https://www.acmicpc.net/problem/18310
# 안테나

n = int(input())
data = list(map(int, input().split()))

data.sort()
mid = n//2-1
print(data[mid])
