def solution(n):
    answer = 0
    if int(n**0.5) == n**0.5: # n이 제곱근인지 판단한다.
        return ((n**0.5)+1)**2 # 양의 정수 제곱일 경우
    else: # 양의 정수 제곱이 아닐경
        return -1
    return answer

print(solution(16))