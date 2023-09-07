def solution(x, n):
    answer = [] # 저장 배열
    for i in range(1, n+1): # 1부터 n번까지 반복 실행
        answer.append(i*x) # answer 마지막에 x*i ex) 3, 3 이면 3*1, 3*2, 3*3 >> [3, 6, 9]
    return answer

print(solution(3,3))