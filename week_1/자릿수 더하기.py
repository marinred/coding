def solution(n):
    answer = 0
    
    num = list(str(n)) # num은 str을 list화 한다. 
    for num in str(n):
        answer += int(num) # num을 int화 하여 각각 더해준다.

    return answer

#* 출력 시도
print(solution(112233))