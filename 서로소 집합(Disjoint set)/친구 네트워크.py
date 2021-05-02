# 노드가 번호가 아닌 문자열일 때 딕셔너리를 사용해 서로소 집합을 구현하는 방법을 알 수 있었다.
# 또한 집합이 몇 개로 구성되어 있는지에 대한 알고리즘을 알 수 있었다.
t = int(input())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a  # 뒤에 있는 부모 노드를 앞에 것으로 갱신
        num[a] += num[b]  # 노드의 개수를 합쳐준다.


for _ in range(t):
    f = int(input())

    # 문자열은 딕셔너리를 사용해 union_find 구현 가능
    # {key = value} 형태로 저장 가능
    # {자식 = 부모}
    parent = {}
    num = {}  # 개수를 세기 위한 딕셔너리
    for i in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a  # 부모와 자식을 자기 자신으로 초기화
            num[a] = 1  # 개수 초기화
        if b not in parent:
            parent[b] = b
            num[b] = 1
        union(parent, a, b)
        print(num[find(parent, a)])

"""
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 
이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

예제 입력 1 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
예제 출력 1 
2
3
4
2
2
4
예제 입력 2
2
3
Fred Barney
Betty Barney
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
예제 출력 2
"""