x = list(input().split(', '))  # ','+'공백' 을 기준으로 문자열을 나눠준다.
n = len(x)
# 첫 번째 원소에서 공통 변수형과 뒤의 변수를 구분지어준다.
start = list(x[0].split())[0]  # 공통 변수형
x[0] = list(x[0].split())[1]
x[-1] = x[-1][:-1]  # 맨 끝에는 세미클론(;)이 붙으므로 이를 지워준다.

for i in range(n):
    ans = start  # 공통 변수형 + 추가 변수형
    ans2 = ''  # 변수 이름
    for j in range(len(x[i])-1, -1, -1):  # 추가변수형들은 거꾸로 공통 변수형 뒤에 붙여준다.
        if x[i][j] == '&' or x[i][j] == '*':
            ans += x[i][j]
        elif x[i][j] == ']':
            ans += '['
        elif x[i][j] == '[':
            ans += ']'
        else:  # 변수 이름은 앞에서부터 저장한다.
            ans2 = x[i][j] + ans2
    # 공통 변수형 + 추가 변수형 + (공백) + 변수 이름 + ';'
    print(ans + ' ' + ans2 + ';')

# 문제 : https://www.acmicpc.net/problem/3568
