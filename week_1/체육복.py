# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    
    reserve_del = set(reserve) - set(lost) # 진짜로 여분을 가진 사람들
    lost_del = set(lost) - set(reserve) # 진짜로 잃어버린 사람들
    
    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
            
    return n - len(lost_del)