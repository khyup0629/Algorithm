# 해시를 이용하는 방법
def solution(phone_book):
    answer = True
    n = len(phone_book)
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 0

    for number in phone_book:
        temp = ''
        for num in number[:-1]:
            temp += num
            # 리스트를 탐색하는 것에 비해 시간 복잡도가 훨씬 줄어든다.
            if temp in hash_map:
                return False

    return answer


# 리스트만 이용하는 방법 (시간 초과)
# 해시에서 탐색하는 것이 시간 복잡도를 훨씬 줄임.
def solution(phone_book):
    answer = True
    n = len(phone_book)

    for number in phone_book:
        temp = ''
        for num in number[:-1]:
            temp += num
            if temp in phone_book:
                return False

    return answer

# 정렬 시켜서 구하는 방법
def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(n - 1):
        # 이렇게 replace한 값을 다른 변수에 지정하면 원래 값은 바뀌지 않음.
        # sort의 경우 phone_book.sort()를 수행하는 것만으로도 원래 phone_book이 정렬된다.
        # x=sorted(phone_book)을 하게 되면 phone_book은 정렬이 안되면서 x에는 정렬된 값이 들어간다.
        result = phone_book[i + 1].replace(phone_book[i], '*')
        if result[0] == '*':
            return False
        # if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        #       return False
        # 조건문으로도 구현 가능.

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42577#
