7n = int(input())
tt = list()
ans = 0

for i in range(n) :
  new_li = list(map(int, input().split()))
  tt.append(new_li)


tt.sort() # 일찍시작 | 빨리끝나는 순으로 정렬
print(tt)

mt_idx = 0 # 현재 회의 중인 idx
cur_time = tt[0][0] # 현재 시간
remain_time = int() # 현재 시간 기준으로 남은 회의 시간

for i in range(1, len(tt)) : 
  # 0부터 끝까지 비교할 인덱스를 계속 증가
  # print("idx : ", i)
  i_dur = tt[i][1] - tt[i][0] # 비교할 회의의 회의시간
  cur_time = tt[i][0] # 현재 시간은 새로 비교할 회의의 시작시간으로 한다.
  remain_time = tt[mt_idx][1] - cur_time # 0이나 음수면 기존의 회의 끝난 것

  if remain_time <= 0 : # 이미 회의가 끝난 경우 회의실을 넘겨준다.
    ans += 1
    mt_idx = i
    remain_time = i_dur
    # print("이미 기존 회의가 끝나 있었어서 넘김")
    continue

  if tt[mt_idx][0] == tt[i][0] : # 비교할 회의의 시작시간이 현재와 같다면 넘김 
    # print("시작 시간이 같아서 pass")
    continue
  
  
  if tt[mt_idx][0] <= tt[i][0] < tt[mt_idx][1] : # 중간에 껴있는 회의
    if i_dur < remain_time : # 비교할 회의의 시간이 더 짧다면 회의실 넘김
        mt_idx = i
        remain_time = i_dur
        # print("새 회의가 더 빨리 끝나서 넘김")
        # 넘겨받은 회의에 대해 검사해야 함

# 마지막 처리가 안된 부분
cur_time = tt[len(tt)-1][1] # 현재 시간은 새로 비교할 회의의 시작시간으로 한다.
remain_time = tt[mt_idx][1] - cur_time # 0이나 음수면 기존의 회의 끝난 것

if remain_time <= 0 : # 이미 회의가 끝난 경우 회의실을 넘겨준다.
  ans += 1
  # print("이미 기존 회의가 끝나 있었어서 넘김!")

print(ans)
