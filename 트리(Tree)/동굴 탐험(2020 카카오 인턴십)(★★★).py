import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, path, order):
    answer = True

    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    # 우선순위의 부모 노드 구하기
    parent = [[] for _ in range(n)]
    lst = []
    for a, b in order:
        parent[b].append(a)
        lst.append(b)

    # 우선 순위를 제외한 나머지 노드들의 부모 노드 구하기
    def set_parent(cur, parent_node):
        for next_node in graph[cur]:
            if next_node == parent_node:
                continue
            parent[next_node].append(cur)
            set_parent(next_node, cur)

    set_parent(0, -1)  # parent 리스트에 인덱스를 자식으로 가지는 부모 노드가 기록되었다.

    # 사이클이 존재하는지 확인하는 함수
    def is_cycle(cur, visited, recur):
        if visited[cur]:  # 바로 들어온 현재 노드(cur)가 이미 방문 되었다면 사이클이 존재
            return True
        if recur[cur]:  # 재귀함수를 통해서 이전에 현재 노드(cur)에서 사이클 검사를 한 적이 있는지
            return False  # 효율성을 개선 시켜주는 기능

        visited[cur] = True
        recur[cur] = True  # 현재 노드에서 사이클 검사를 한 적이 있다
        # cur = 0 이라면, for문을 스킵하게 된다.
        for parent_node in parent[cur]:  # 현재 노드에서 갈 수 있는 부모 노드중 한 노드
            if is_cycle(parent_node, visited, recur):  # 부모 노드로 거슬러 올라간다.
                return True

        visited[cur] = False  # 이 줄이 없으면 이전에 방문했던 곳들이 전부 방문완료 처리가 된다.
        # 중간에 True값을 반환하지 않고 내려왔다면 사이클이 없다는 뜻이다.
        return False

    visited = [False] * n
    recur = [False] * n
    for i in lst:
        if is_cycle(i, visited, recur):
            return False

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/67260
