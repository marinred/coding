def solution(n, arr1, arr2):

    answer = []
    for i in range(n):
        row1 = bin(arr1[i])[2:].zfill(n)
        row2 = bin(arr2[i])[2:].zfill(n)
        answer.append('')
        for y in range(n):
            if row1[y] == '0' and row2[y] == '0':
                answer[i] += ' '
            elif row1[y] == '1' or row2[y] == '1':
                answer[i] += '#'

    return answer