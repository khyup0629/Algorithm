# PyPy3 제출 > 메모리 : 130608 KB, 시간 : 260 ms
# 파이썬 제출 > 메모리 : 29556 KB, 시간 : 4920 ms
# 문자열에서 result = result[:-1] 이렇게 하면 계산 시간이 많이 소요되는 것을 알았다.
k = int(input())

result = []
for i in range(k):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop()

print(sum(result))

"""
# 계산 시간이 많이 소요되는 코드
k = int(input())

result = []
for i in range(k):
    num = int(input())
    result.append(num)
    # 이 부분에 의해 계산 시간이 많이 소요됨
    result = result[:-2] if num == 0 else result

print(sum(result))
"""