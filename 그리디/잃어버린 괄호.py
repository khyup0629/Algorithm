# '+'를 우선적으로 더해준 후 나머지 '-'계산
# 즉, '-'를 기준으로 구역을 나눈 뒤 덧셈 먼저 계산 후 각 구역 뺄셈

exp = input().split('-')
result = 0

# [15, 15+20, 30+40+25] 이런 식으로 리스트 형성

for i in map(int, exp[0].split('+')):
    result += i

# 리스트 첫 항 계산

for i in exp[1:]:
    result -= sum(map(int, i.split('+')))

# 리스트 두 번째 항부터 각 항의 +를 제거하고 숫자를 모두 더한 후 result에 빼준다.
# sum(리스트) : 리스트 각 항의 숫자들을 모두 더해준다.
# 문자열.split('기준') : 문자열을 기준으로 분리해서 리스트로 만든다.
print(result)
