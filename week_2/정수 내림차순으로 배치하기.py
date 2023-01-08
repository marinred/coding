# 정수 내림차순으로 배치하기

def solution(n):
    answer = sorted(list(str(n)), reverse=True)
    return int(''.join(answer))

# 테스트 결과
print(solution(12345))