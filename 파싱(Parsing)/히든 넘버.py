n = int(input())
s = input()

num = []
changed = False  # 탐색 범위가 숫자 범위인지 여부
number = ''
for i in range(n):
    if s[i].isalpha():  # 문자라면,
        if changed:  # 이전까지가 숫자였다면,
            changed = False
            num.append(int(number))
        continue
    else:  # 숫자라면,
        if not changed:  # 이전까지 문자였다면,
            number = s[i]
            changed = True
        else:  # 이전에도 숫자였다면,
            number += s[i]
    if i == n - 1 and s[i].isdigit():  # 마지막 글자를 탐색할 때, 숫자에서 끝난다면,
        num.append(int(number))  # number 에 저장된 숫자를 추가

print(sum(num))

# 문제 : https://www.acmicpc.net/problem/8595
