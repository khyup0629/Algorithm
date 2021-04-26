# count 로 찾게 되면 당연히 시간 초과가 나온다
# 이진 탐색이나 집합을 생각할 수 있는데 간단하게 집합을 이용하면 되었다.
# &(and) 연산자를 사용해 교집합을 취하면 된다.

n, m = map(int, input().split())

hear = [input() for _ in range(n)]
see = [input() for _ in range(m)]

# set 만 사용하면 {}로 묶여서 클래스의 형태로 나오게 되는데
# 이를 list 를 바깥에 씌움으로써 리스트로 만들 수 있다.
result = list(set(hear) & set(see))

print(len(result))
for i in sorted(result):
    print(i)

"""
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

 

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

예제 입력 1 
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
예제 출력 1 
2
baesangwook
ohhenrie
"""