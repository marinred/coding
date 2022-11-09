def solution(s):
    dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for i in dict.items(): # .items함수를 사용하면 dict의 key,value를 얻을 수 있다. (.items 사용방법을 몰랐습니다.)
        s = s.replace(i[0],i[1])
        
    answer = int(s)
    return answer

# 결과값 
# print(solution("1twonine4zero"))
# >> 12940