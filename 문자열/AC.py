# (시간 : 212ms)
# R이 나오는대로 리버스를 시행하면 시간 복잡도가 어마어마하게 증가된다.
# 1. RR이 나오면 원래 상태와 같음.
# 2. 원 상태에서 D는 첫 번째 원소를 지우고, RD은 마지막 원소를 지운다.
# fun 를 한 문자씩 수행하지 말고 최대한 모아뒀다가 수행.
# num.remove(num[0]), num.pop() 역시 O(n)의 시간 복잡도를 가진다.
# 따라서 한 번에 모아뒀다가 처리하는 방식을 취하면 시간 복잡도를 더 줄일 수 있다.

t = int(input())

for _ in range(t):
    fun = input()
    fun.replace('RR', '')
    n = int(input())
    array = input()[1:-1]
    num = [] if array == '' else list(array.split(','))
    rev = False  # 리버스 상태 여부
    left, right = 0, 0  # 왼쪽과 오른쪽의 원소를 지울 때 한 번에 지우기 위함.
    for word in fun:
        if word == 'R':
            rev = not rev  # 리버스 상태를 바꿔준다.
        elif word == 'D':
            if not rev:  # 리버스 상태가 아니면,
                left += 1  # 왼쪽을 지운다.
            else:
                right += 1  # 오른쪽을 지운다.

    if (left + right) > n:  # 원래 길이보다 지워야 하는 개수가 더 길다면 에러
        print('error')
    else:
        # left, right 만큼 num 에서 지운다.
        ans = num[left:n-right]
        if rev:  # 리버스 상태라면 리버스 시켜서 출력
            ans.reverse()
        print('[' + ','.join(ans) + ']')

"""
(시간 : 3788ms)
# R이 나오는대로 리버스를 시행하면 시간 복잡도가 어마어마하게 증가된다.
# 1. RR이 나오면 원래 상태와 같음.
# 2. 원 상태에서 D는 첫 번째 원소를 지우고, RD은 마지막 원소를 지운다.
# fun 를 한 문자씩 수행하지 말고 최대한 모아뒀다가 수행.

t = int(input())

for _ in range(t):
    fun = input()
    fun.replace('RR', '')  # RR이 나오면 원래 상태와 같음.
    n = int(input())
    array = input()[1:-1]
    num = [] if array == '' else list(array.split(','))
    Er = False  # 에러 발생 여부
    rev = False  # 리버스 상태 여부
    for word in fun:
        try:
            if word == 'R':
                rev = not rev
            elif word == 'D':
                if not rev:
                    num.remove(num[0])
                else:
                    num.pop()
        except:
            Er = True
            break

    if Er:
        print('error')
    else:
        if rev:
            num.reverse()
        ans = '[' + ','.join(num) + ']'
        print(ans)
"""
"""
문제
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 
만약, 에러가 발생한 경우에는 error를 출력한다.

예제 입력 1 
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
예제 출력 1 
[2,1]
error
[1,2,3,5,8]
error
예제 입력 2
1
RDD
2
[15,27]
예제 출력 2
[]
예제 입력 3
1
R
2
[15,27]
예제 출력 3
[27,15]
"""
