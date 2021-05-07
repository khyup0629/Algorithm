from itertools import permutations
import math


def solution(numbers):
    answer = 0

    numbers = list(map(str, numbers))
    n = len(numbers)

    def prime_number(x):  # 소수 판별
        if x == 1 or x == 0:  # 0~9의 정수는 1과 0은 소수가 아니다.
            return False
        # 2와 3은 for문을 뛰어넘어 그대로 True로 출력된다.
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    prime = {}  # 딕셔너리로 받아서 탐색시간을 O(1)로 만든다.
    for i in range(1, n + 1):
        permu = list(permutations(numbers, i))  # 입력값이 8이하이므로 permutations 사용 가능.
        for j in permu:
            result = ''
            for k in j:
                result += k
            # 소수이면서, 기존에 구한 소수와 중복되지 않는다면,
            if prime_number(int(result)) and int(result) not in prime:
                prime[int(result)] = int(result)
                answer += 1

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42839#
