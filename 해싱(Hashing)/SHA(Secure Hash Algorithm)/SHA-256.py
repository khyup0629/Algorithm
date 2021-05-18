import hashlib

word = input()
print(hashlib.sha256(word.encode()).hexdigest())
