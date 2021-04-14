# 금방 푼 문제

T = int(input())

result_score = []
for k in range(T):
    # 하나의 문자열을 음절로 쪼개기
    string = list(input())

    score = 0
    value = 1
    # 초기값, 이후 반복문에서 인덱스 1부터 고려하기 위함
    if string[0] == 'O':
        score += value
    for i in range(1, len(string)):
        if string[i] == 'X':
            # 가중치 초기화
            value = 1
            continue
        else:
            if string[i-1] == 'O':
                # 가중치 1씩 더해주기
                value += 1
                score += value
            else:
                # X 이후 첫 번째 O라는 뜻
                score += value
    result_score.append(score)

for i in result_score:
    print(i)

"""
문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.

예제 입력 1 
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
XOOXO
예제 출력 1 
10
9
7
55
4
"""