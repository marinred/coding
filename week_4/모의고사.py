def solution(answers):
    answer = []
    person = [0] * 3
    person_one = [1,2,3,4,5]
    person_two = [2,1,2,3,2,4,2,5]
    person_three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == person_one[i%5]: # 첫 번째 인원은 5개의 답이 반복
            person[0] += 1
        if answers[i] == person_two[i%8]: # 두 번째의 인원은 8개의 답이 반복
            person[1] += 1
        if answers[i] == person_three[i%10]: # 세 번째의 인원은 5개의 답이 반복
            person[2] += 1
            
    winner = max(person)
    
    for i in range(len(person)):
        if person[i] == winner:
            answer.append(i+1)
    return answer