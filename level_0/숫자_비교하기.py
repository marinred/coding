def solution(num1, num2):
    answer = 0
    if num1 == num2:
        return 1
    else:
        return -1

# lambda 형식의 숫자 비교하기
solution = lambda num1, num2: 1 if num1 == num2 else -1

print(solution(10, 22))
print(solution(22, 22))