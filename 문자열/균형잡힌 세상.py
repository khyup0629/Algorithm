# 다른 아이디어 코드
# 1. 왼쪽 괄호들은 모두 임시 저장소에 저장하고 오른쪽 괄호가 나왔을 때
# 왼쪽 괄호와 종류가 같다면 임시 저장소의 가장 최근 왼쪽 괄호를 지운다.
# 종류가 다르다면 즉시 문자열 탐색을 멈추고 'no'
# 2. 임시 저장소에 왼쪽 괄호가 남아있지 않다면 'yes'

while True:
    sentence = input()
    if sentence == '.':  # 반복 종료
        break
    temp = []  # 왼쪽 괄호가 저장될 임시 저장소
    balance = True  # 괄호의 1대 1 조건 만족 여부
    for word in sentence:
        if word == '(' or word == '[':
            temp.append(word)  # 왼쪽 괄호면 저장
        elif word == ')':
            if not temp or temp[-1] != '(':
                balance = False
                break  # 저장소가 비었거나 가장 최근 왼쪽 괄호와 종류가 다르다면 탐색 종료
            else:
                temp.pop()  # 가장 최근 왼쪽 괄호와 같은 종류라면 지운다.
        elif word == ']':
            if not temp or temp[-1] != '[':
                balance = False
                break  # 저장소가 비었거나 가장 최근 왼쪽 괄호와 종류가 다르다면 탐색 종료
            else:
                temp.pop()  # 가장 최근 왼쪽 괄호와 같은 종류라면 지운다.
    # 괄호가 1대 1 대응이 되면서 왼쪽, 오른쪽 개수가 서로 같아서 저장소가 비어있다면
    if balance and not temp:
        print('yes')
    else:
        print('no')

"""
# 기존 나의 코드, 위는 다른 아이디어 코드
# 문제를 푸는 핵심 아이디어
# 1. (베이스 아이디어) 소괄호와 대괄호의 왼쪽, 오른쪽 개수가 각각 문장 내에서 같으면 'yes', 다르면 'no'
# 2. (중간중간 고려할 조건) 오른쪽 괄호가 나올 때 가장 최근에 나온 왼쪽 괄호와 종류가 같아야 한다.

while True:
    cnt_small_left, cnt_small_right = 0, 0  # '(', ')' 개수
    cnt_big_left, cnt_big_right = 0, 0  # '[', ']' 개수
    sentence = input()
    if sentence == '.':  # 반복문 종료 조건
        break
    temp = []  # 왼쪽 괄호들을 임시로 저장한다.
    for word in sentence:
        if word == '(':
            cnt_small_left += 1
            temp.append(word)
        elif word == ')':
            # 가장 최근에 나온 왼쪽 괄호와 같은 종류이면
            # 정상적으로 진행시키고 임시 저장소의 최근에 나온 왼쪽 괄호를 지운다.
            if not temp or temp[-1] != '(':
                cnt_small_right += 1
                break
            # 종류가 다르다면 균형이 맞지 않는 문장이므로 카운트를 +1하고 반복 종료
            # 카운트를 +1 하는 이유는 지금까지 ')'까지 탐색했기 때문에 카운트 해주는 것
            else:
                cnt_small_right += 1
                temp.pop()
        elif word == '[':
            cnt_big_left += 1
            temp.append(word)
        elif word == ']':
            if not temp or temp[-1] != '[':
                cnt_big_right += 1
                break
            else:
                cnt_big_right += 1
                temp.pop()
    if cnt_small_left != cnt_small_right or cnt_big_left != cnt_big_right:
        print('no')
    if cnt_small_left == cnt_small_right and cnt_big_left == cnt_big_right:
        print('yes')
"""
"""
문제
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

입력
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 
길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

예제 입력 1 
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
예제 출력 1 
yes
yes
no
no
no
yes
yes
"""