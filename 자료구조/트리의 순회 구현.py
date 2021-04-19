class Node:
    def __init__(self, root, left_node, right_node):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Pre-order Traversal) : 루트 노드 제일 먼저
def pre_order(node):
    # 루트 먼저
    print(node.root, end=' ')
    # 왼쪽 끝까지 들어갔다가
    if node.left_node != None:
        pre_order(tree[node.left_node])
    # 오른쪽 마지막
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(In-order Traversal) : 왼쪽부터 우선순위로 보고 두번째 우선순위가 루트 노드
def in_order(node):
    # 왼쪽 끝까지 먼저 들어가서
    if node.left_node != None:
        in_order(tree[node.left_node])
    # 루트 노드 출력
    print(node.root, end=' ')
    # 오른쪽 자식 노드 출력
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Post-order Traversal) : 왼쪽부터 우선순위로 보고, 그 다음 막히면 오른쪽 노드
# 마지막으로 루트 노드
def post_order(node):
    # 왼쪽 끝까지 먼저 들어가서
    if node.left_node != None:
        post_order(tree[node.left_node])
    # 오른쪽 자식 노드
    if node.right_node != None:
        post_order(tree[node.right_node])
    # 루트 노드
    print(node.root, end=' ')


n = int(input())
tree = {}

for i in range(n):
    root, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[root] = Node(root, left_node, right_node)

print(tree)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

"""
예제 입력
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
예제 출력
A B D E C F G 
D B E A F C G 
D E B F G C A 
"""