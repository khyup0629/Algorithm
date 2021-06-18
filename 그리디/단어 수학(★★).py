# 문제 풀이 아이디어
# 1. 딕셔너리를 만들어서 알파벳의 해시값을 모두 0으로 둔다.
# 2. 각 문자의 알파벳이 언급된만큼 10^(자릿수-1)을 해시를 통해서 더해준다.
# (알파벳에 가중치를 둔다)
# 3. 딕셔너리에서 0이 아닌 알파벳은 한 번이라도 언급이 되었단 뜻이므로 그 value를 뽑아낸다.
# 4. value를 내림차순으로 정렬한다.
# 5. value를 하나씩 뽑아내서 9부터 -1씩한 값을 차례로 곱하면서 그 값들을 모두 더해준다.
n = int(input())
# 1. 딕셔너리를 만들어서 알파벳의 해시값을 모두 0으로 둔다.
alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
         'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
string = [input() for _ in range(n)]

for i in string:
    for j in range(len(i)):
        # 2. 각 문자의 알파벳이 언급된만큼 10^(자릿수-1)을 해시를 통해서 더해준다.
        num = 10 ** (len(i)-1-j)
        alpha[i[j]] += num

# 3. 딕셔너리에서 0이 아닌 알파벳은 한 번이라도 언급이 되었단 뜻이므로 그 value를 뽑아낸다.
lst = []
for i in alpha.values():
    if i > 0:
        lst.append(i)

# 4. value를 내림차순으로 정렬한다.
lst.sort(reverse=True)
# 5. value를 하나씩 뽑아내서 9부터 -1씩한 값을 차례로 곱하면서 그 값들을 모두 더해준다.
result = 0
for i in range(9, 9-len(lst), -1):
    result += lst[9-i] * i

print(result)

# 문제 : https://www.acmicpc.net/problem/1339
