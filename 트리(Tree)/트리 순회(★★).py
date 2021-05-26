class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def preorder_traversal(node):  # 전위 순회
    global ans
    ans += node
    if tree[node].left:
        preorder_traversal(tree[node].left)
    if tree[node].right:
        preorder_traversal(tree[node].right)


def inorder_traversal(node):  # 중위 순회
    global ans
    if tree[node].left:
        inorder_traversal(tree[node].left)
    ans += node
    if tree[node].right:
        inorder_traversal(tree[node].right)


def postorder_traversal(node):  # 후위 순회
    global ans
    if tree[node].left:
        postorder_traversal(tree[node].left)
    if tree[node].right:
        postorder_traversal(tree[node].right)
    ans += node


n = int(input())

tree = {}
for _ in range(n):
    parent, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[parent] = Node(left, right)

ans = ''
preorder_traversal('A')
print(ans)

ans = ''
inorder_traversal('A')
print(ans)

ans = ''
postorder_traversal('A')
print(ans)

# 문제 : https://www.acmicpc.net/problem/1991
