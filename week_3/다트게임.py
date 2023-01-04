# 다트게임

def solution(dartResult):
    nums = []
    temp = 0
    strNums = 0
    
    for i in dartResult:
        if "0" <= i <= "9":
            temp = temp * 10 + int(i)
        elif i == "S":
            nums.append(temp)
            temp = 0
            strNums += 1
        elif i == "D":
            nums.append(temp** 2)
            temp = 0
            strNums += 1
        elif i == "T":
            nums.append(temp ** 3)
            temp = 0
            strNums += 1
        elif i == "*":
            if strNums > 1:
                nums[strNums - 2] *= 2
            nums[strNums - 1] *= 2
        elif i == "#":
            nums[strNums - 1] *= -1
    return sum(nums)

print(solution("10S10D10T*"))
    