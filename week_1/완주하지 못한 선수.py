# 이진법
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# n = 5
# for i in range(len(arr1)):
#     bin1 = bin(arr1[i])[2:].zfill(n)
#     bin2 = bin(arr2[i])[2:].zfill(n)
# print(bin1)
# print(bin2)

# 해시
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))


# sorted
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
print("sorted data: ", sorted(arr))
print("input data: ", arr)
# sort()
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
arr.sort()
print("input data: ", arr)

# sorted 배열 자체를 조작하지 않음
# sort는 배열 자체를 바꿔준다.