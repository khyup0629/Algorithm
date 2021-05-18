import hashlib

word = input()
print(hashlib.sha512(word.encode()).hexdigest())

# 문제 : https://www.acmicpc.net/problem/10932
