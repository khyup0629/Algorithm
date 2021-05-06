# 분할 정복 유형의 알고리즘을 처음 접했다.
# eval(문자열) 함수를 안다면 그나마 쉽게 아래와 같은 방법으로 해결할 수 있다.
# eval(문자열) : 문자열 수식(ex. eval('100+50') = 150)을 계산해준다.
def dfs(priority, n, expression):
    ans = []
    if n == 0:
        return str(eval(expression))
    if priority[n] == '*':
        for e in expression.split('*'):
            ans.append(dfs(priority, n - 1, e))
        return str(eval('*'.join(ans)))
    if priority[n] == '+':
        for e in expression.split('+'):
            ans.append(dfs(priority, n - 1, e))
        return str(eval('+'.join(ans)))
    if priority[n] == '-':
        for e in expression.split('-'):
            ans.append(dfs(priority, n - 1, e))
        return str(eval('-'.join(ans)))


def solution(expression):
    answer = 0

    m = [('*', '+', '-'), ('*', '-', '+'), ('+', '*', '-'), ('+', '-', '*'), ('-', '*', '+'), ('-', '+', '*')]

    result = []
    for priority in m:
        result.append(abs(int(dfs(priority, 2, expression))))

    answer = max(result)
    return answer

# 문제 링크
# https://programmers.co.kr/learn/courses/30/lessons/67257
