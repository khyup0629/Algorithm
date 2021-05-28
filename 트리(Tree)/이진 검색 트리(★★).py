# 아이디어는 생각했으나 효율적 코드 구현이 힘들었던 문제.
# 문제 풀이 아이디어
# 1. 전위 순회의 첫 번째 원소가 최상단 노드
# 2. 이를 기준으로 전위 순회 리스트를 탐색하면서 기준보다 큰 값의 인덱스를 찾는다.
# 3. 찾은 인덱스를 기준으로 왼쪽부와 오른쪽부로 나눠서 DFS 진행
# 4. (★)후위 순회이므로 마지막에 현재 노드(pre_order[start])를 출력하면 된다.
import sys
sys.setrecursionlimit(10**5)

pre_order = []
while True:
    try:
        num = int(input())
        pre_order.append(num)
    except:
        break

n = len(pre_order)


def dfs(start, end):
    if start > end:
        return
    parent = pre_order[start]
    i = start + 1
    while i <= end:
        if parent < pre_order[i]:
            break
        i += 1

    dfs(start + 1, i - 1)
    dfs(i, end)

    print(parent)


dfs(0, n-1)

# 문제 : https://www.acmicpc.net/problem/5639
