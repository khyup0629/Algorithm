def solution(s):
    n = len(s)

    result = []  # i개씩 분해해서 압축한 문자열 모두 저장
    # i개씩 문자열 분해
    for i in range(1, n + 1):
        temp = []
        s_now = ''
        for j in range(n):
            s_now += s[j]
            if j % i == i - 1:  # i개씩 잘라서
                temp.append(s_now)  # temp에 저장
                s_now = ''  # 초기화
        temp.append(s_now)  # 남은 문자열 추가

        cnt = 1
        s_temp = ''
        for j in range(1, len(temp)):
            if temp[j] == temp[j - 1]:  # j-1과 j 비교
                cnt += 1  # 같으면 +1
            else:  # j-1과 j가 다르면
                # 앞에서 반복된 갯수만큼 접두, 1이면 생략
                num = (str(cnt) if cnt > 1 else '')
                s_temp += (num + temp[j - 1])
                cnt = 1  # 초기화
        # 마지막 항까지 처리
        num = (str(cnt) if cnt > 1 else '')
        s_temp += (num + temp[-1])

        result.append(s_temp)

    answer = min(result, key=lambda x: len(x))  # 문자열 길이 기준 가장 작은값

    return len(answer)  # 최소 길이

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/60057#
