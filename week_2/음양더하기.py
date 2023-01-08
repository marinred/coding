# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i] # signs[i]가 True
        else:
            answer -= absolutes[i] # signs[i]가 False
            
    return answer

print(solution([1, 33, 199], [False, False, True]))