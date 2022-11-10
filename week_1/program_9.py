def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer

#! 출력값
print(solution([1,2,3,4,5])) # 결과값 30 나옴