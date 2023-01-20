def solution(phone_number):
    for i in range(len(phone_number)-4):
        phone_number = phone_number.replace(phone_number[i], '*',1)
    return phone_number


# replace를 이용하여 마지막 4자리를 제외한 숫자들을 *로 바꾸고 return