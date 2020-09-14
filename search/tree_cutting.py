# 백준 2805 - 나무 자르기
# python search/tree_cutting.py
## 입력
# 4 7
# 20 15 10 17
## 출력
# 15

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 최대한 덜 잘랐을 때가 정답이므로, end 값을 줄일 때 마다 result에 기록
result = 0
def binary_search(arr, target, start, end):
  while start <= end:
    h = (start + end) // 2
    total = 0
    for tree in arr:
      # 나무가 절단기 높이보다 클때만 ! 자른다
      if tree > h:
        total += tree - h
    if total < target:
      end = h - 1
    else:
      result = h
      start = h + 1
  return result
    
print(binary_search(arr, m, 0, max(arr)))