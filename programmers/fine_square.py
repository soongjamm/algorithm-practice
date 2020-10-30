# 멀쩡한 사각형
# 참고 : https://taesan94.tistory.com/55
from math import gcd

def solution(w,h):

    # 최대공약수를 구한다.
    # w와 h에서 각각 최대공약수를 나눈 숫자 만큼 못 쓰는 블락의 패턴의 위치가 변한다.
    g = gcd(w,h)

    total = w*h # 전체 블락의 개수
    notUsedInAPattern = (w//g)+(h//g) - 1
    answer = total - (notUsedInAPattern * g)
    return answer

print(solution(12,8))