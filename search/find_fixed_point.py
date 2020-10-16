# 고정점 찾기

# 중간점을 타겟으로 간주한다.

def bs(start, end):
  if start > end:
    return None
  mid = (start+end)//2

  if data[mid] == mid:
    return mid
  elif data[mid] > mid:
    return bs(start, mid-1)
  elif data[mid] < mid:
    return bs(mid+1, end)
  

n = int(input())
data = list(map(int, input().split()))

index = bs(0, n-1)

if index == None:
  print(-1)
else:
  print(index)

