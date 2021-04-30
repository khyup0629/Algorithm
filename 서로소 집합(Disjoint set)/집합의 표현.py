# PyPy3는 메모리 초과, Python3는 시간 초과로 코드는 맞았는데 골머리를 썩혔던 문제.
# PyPy3에서 메모리 초과를 이유로 limit(10000)을 하게 되면 런타임 에러가 뜨고
# limit(10000000) 정도로 높게 설정하면 바로 메모리 초과가 뜬다.
# Python3에서는 메모리는 낮으나 시간 초과가 계속해서 발생했다.
# 따라서, Python3로 제출하되 입력 속도를 빠르게 해주는 readline을 넣으니
# 시간 초과 문제가 해결되었다.

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
# 집합의 개수, 연산의 개수
n, m = map(int, input().split())

# 부모 노드
parent = [i for i in range(n+1)]


# 부모 노드 찾기(Find)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 합집합(Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 부모 노드 갱신
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    uf, a, b = map(int, input().split())
    if uf == 0:
        union_parent(parent, a, b)
    else:
        # 서로의 부모 노드가 같으면 같은 집합
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

"""
문제
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 
다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 
이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

출력
1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)

예제 입력 1 
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
예제 출력 1 
NO
NO
YES
"""