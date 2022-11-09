def solution(num):
    num = str(num)
    answer = []
    
    for i in num:
        answer.append(int(i))
    answer = answer[::-1] # 역순 출력
    
    return answer



#todo 결과값 시도
print("결과값 : {}" .format(solution(int(12345))));
# 결과값 : [5, 4, 3, 2, 1]