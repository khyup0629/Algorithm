# set 이라는 함수를 알 수 있었던 문제
# 문자열에서 랜덤으로 문자열의 구성요소를 중복없이 뽑아준다.

sentence = input()
sentence = sentence.upper()
word = list(set(sentence))  # ['M', 'I', 'S', 'P']

result = []
for i in word:
    cnt = sentence.count(i)
    result.append(cnt)

max_cnt = max(result)
print('?' if result.count(max_cnt) > 1 else word[result.index(max_cnt)])

"""
sentence = input()

sentence = sentence.lower()
alpha_index = [0] * 26

for word in sentence:
    alpha_index[ord(word)-97] += 1

max_cnt = max(alpha_index)
print('?' if alpha_index.count(max_cnt) > 1 else chr(alpha_index.index(max_cnt) + 65))
"""