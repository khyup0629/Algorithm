def solve():
    _max = 0
    ans = ''
    while True:
        lst = list(input().split())
        for word in lst:
            if word == 'E-N-D':  # 문장의 끝에 도달하면 답을 출력하고 종료.
                print(ans)
                return
            cnt = 0  # 단어의 철자 개수
            result = ''
            for i in word:
                if i.isalpha() or i == '-':  # 단어가 알파벳으로 이루어져있거나 하이폰(-)이라면
                    result += i.lower()  # 소문자로 넣기
                    cnt += 1  # 단어 철자 개수 세기
            if _max < cnt:  # 단어 철자 개수가 최댓값이라면,
                _max = cnt
                ans = result  # 답(ans)에 단어 넣기


solve()

# 문제 : https://www.acmicpc.net/problem/5637
