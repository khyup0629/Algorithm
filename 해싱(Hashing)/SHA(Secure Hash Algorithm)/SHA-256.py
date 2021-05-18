import hashlib

word = input()
print(hashlib.sha256(word.encode()).hexdigest())

# 문제 : https://www.acmicpc.net/problem/10930
