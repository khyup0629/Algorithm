# 재귀함수를 푸는 것과 다른 풀이 방식
# 코드는 길지만 직관적이다. 숫자와 연산자 리스트를 만들어 따로 분리해놓은 것이 포인트.
def solution(expression):
    answer = 0

    # 숫자와 연산자로 나누기
    number = ''
    mark = []
    num = []
    for i in range(len(expression)):
        if expression[i] in '*+-':
            mark.append(expression[i])
            num.append(number)
            number = ''
        else:
            number += expression[i]
    num.append(number)

    m = [('*', '+', '-'), ('*', '-', '+'), ('+', '*', '-'), ('+', '-', '*'), ('-', '*', '+'), ('-', '+', '*')]

    result = []
    # 우선순위대로 연산자 계산을 한다.
    # 우선순위를 거치면서 결과 리스트를 갱신한다.
    for a, b, c in m:
        # 첫 번째 우선순위 연산 결과 숫자와 연산자 리스트
        result_mark = []
        result_num = [num[0]]  # 초기값
        for i in range(len(mark)):  # 연산자 탐색 시작
            if mark[i] == a:  # 연산자가 우선순위 연산자와 같으면,
                # 결과 숫자 리스트의 마지막 값을 갱신한다.
                result_num[-1] = str(eval(result_num[-1] + a + num[i + 1]))
            else:  # 연산자가 다르면,
                result_mark.append(mark[i])  # 결과 연산자 리스트에 연산자를 추가한다.
                result_num.append(num[i + 1])  # 결과 숫자 리스트에 다음 숫자를 추가한다.
        # 두 번째 우선순위 연산 결과 숫자와 연산자 리스트
        # 위와 같은 방식
        result_mark_2 = []
        result_num_2 = [result_num[0]]  # 초기값
        for i in range(len(result_mark)):
            if result_mark[i] == b:
                result_num_2[-1] = str(eval(result_num_2[-1] + b + result_num[i + 1]))
            else:
                result_mark_2.append(result_mark[i])
                result_num_2.append(result_num[i + 1])
        # 마지막 우선순위 연산 결과 숫자와 연산자 리스트
        result_mark_3 = []
        result_num_3 = [result_num_2[0]]  # 초기값
        for i in range(len(result_mark_2)):
            if result_mark_2[i] == c:
                result_num_3[-1] = str(eval(result_num_3[-1] + c + result_num_2[i + 1]))
            else:
                result_mark_3.append(result_mark_2[i])
                result_num_3.append(result_num_2[i + 1])
        result.append(abs(int(result_num_3[0])))

    answer = max(result)
    return answer

# 문제 링크
# https://programmers.co.kr/learn/courses/30/lessons/67257
