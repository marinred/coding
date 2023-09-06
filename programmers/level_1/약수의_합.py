def solution(n):
    number = [] # 약수 저장 배열
    for i in range(1, n+1):
        if n % i == 0: # 나눴을 때 나머지가 0일 때 약수가 나온다.
            number.append(i) # number에 number append
    return sum(number) # 약수의 합을 return