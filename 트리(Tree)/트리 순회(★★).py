# 딕셔너리를 이용한 풀이
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
n = int(input())

tree = defaultdict(list)  # Class:list 딕셔너리 생성

for _ in range(n):
    parent, child1, child2 = input().split()
    tree[parent].append(child1)
    tree[parent].append(child2)


def preorder(node):  # 전위 순회
    global preorderAns
    preorderAns += node
    if tree[node][0] != '.':
        preorder(tree[node][0])
    if tree[node][1] != '.':
        preorder(tree[node][1])


def inorder(node):  # 중위 순회
    global inorderAns
    if tree[node][0] != '.':
        inorder(tree[node][0])
    inorderAns += node
    if tree[node][1] != '.':
        inorder(tree[node][1])


def postorder(node):  # 후위 순회
    global postorderAns
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])
    postorderAns += node


preorderAns = ''
preorder('A')
print(preorderAns)
inorderAns = ''
inorder('A')
print(inorderAns)
postorderAns = ''
postorder('A')
print(postorderAns)

# class를 이용한 풀이
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
