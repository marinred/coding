def solution(arr_1, arr_2):
    answer = []
    for i in range(len(arr_1)):
        tmp = []
        for j in range(len(arr_1[0])):
            tmp.append(arr_1[i][j] + arr_2[i][j])
        answer.append(tmp)
    return answer