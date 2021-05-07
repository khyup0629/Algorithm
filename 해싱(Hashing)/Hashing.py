l = int(input())
string = input()


def hashing(string, l):
    # 알파벳 소문자에 대응하는 고유 번호 기록.
    hash_map = {}
    for i in range(1, 27):
        hash_map[chr(96+i)] = i

    array = []
    for i in string:
        array.append(hash_map[i])

    # i : 0 ~ l-1 에서 각 array[i] * (r^i)를 모두 더한다.
    _sum = 0
    for i in range(l):
        _sum += array[i] * (31 ** i)

    # M(1234567891)으로 나눈 나머지가 해시 값(h)이다.
    h = _sum % 1234567891
    return h


print(hashing(string, l))

# 문제 : https://www.acmicpc.net/problem/15829
