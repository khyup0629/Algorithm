# 자연수를 1부터 더해간 값이 최초로 s를 넘어갈 때
# 넘어간만큼의 차이를 빼주면 된다.
# S의 입력값의 범위가 최대 4,294,967,295였는데 이 값은
# 약 92681까지의 수를 모두 더한 것이다.
# 따라서, 시간복잡도를 O(N)으로 두고 풀어야 했다.
s = int(input())

i = 1
result = 0
while True:
    result += i
    if result > s:
        print(i-1)
        break
    i += 1

"""
for i in range(1, 1000000):
    if (i * (i + 1)) / 2 > 4294967295:
        print(i)
        break
"""
