# 서로 다른 nums의 원소 3개를 골라 더했을 때 소수가 되는 경우 return
# def check(a, b, c):
#     total = a + b + c
#     for i in range(2, total // 2 + 1):
#         if total % i == 0: return False
#     return True

# def solution(nums):
#     answer = 0
#     for i in range(0, len(nums) - 2):
#         for j in range(i + 1, len(nums) - 1):
#             for k in range(j + 1, len(nums)):
#                 if check(nums[i], nums[j], nums[k]): answer += 1
#     return answer

# 위의 경우 for문이 너무 많음

# combinations를 이용한 코드

from itertools import combinations
# combinations: 하나의 리스트에서 모든 조합을 구하기

def check(a, b, c):
    total = a + b + c
    for i in range(2, total // 2 + 1):
        if total % i == 0: return False
    return True

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)): 
        if check(i[0], i[1], i[2]): answer += 1
    return answer