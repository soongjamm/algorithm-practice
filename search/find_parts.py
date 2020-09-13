# 1. binary search
n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

def find_parts(arr, target, start, end):
  if start > end:
    return None
  
  mid = (start+end) // 2

  if arr[mid] == target:
    return 'Yes'
  elif arr[mid] < target:
    return find_parts(arr, target, mid+1, end)
  else:
    return find_parts(arr, target, start, mid-1)

narr.sort()
marr.sort()
for i in range(m):
  res = find_parts(narr, marr[i], 0, n-1)
  if res:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')

print()