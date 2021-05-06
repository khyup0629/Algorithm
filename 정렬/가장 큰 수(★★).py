def solution(numbers):
    answer = ''

    numbers = [str(i) for i in numbers]
    # 문자열 숫자 비교는 문자열의 각 인덱스끼리 대응해서 비교한다.(ASCII 코드로 변환되어 비교됨)
    numbers.sort(key=lambda x: x + x + x, reverse=True)

    for i in numbers:
        answer += i
    return str(int(answer))  # (숨겨진 조건)만약 answer = "0000000"일 경우 "0"이 반환되어야 한다.

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42746#
