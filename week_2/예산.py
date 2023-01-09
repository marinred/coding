def solution(d, budget):
    answer = 0
    for i in sorted(d): # sorted(정렬할 데이터) for문을 이용하여 budget을 빼준다.
        budget -= i
        if budget < 0: # budget이 0보다 작다면 break
            break
        answer += 1
        
    return answer