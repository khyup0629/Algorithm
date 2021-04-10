import time
start_time = time.time() # 측정 시작

N = int(input())

result = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if s % 10 == 3 or s // 10 == 3 or m % 10 == 3 or m // 10 == 3 or h % 10 == 3:
                result += 1

print(result)

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

'''
# 색다른 방법
N = int(input())

result = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
        # 시, 분, 초를 문자열로 만들어서 모두 더해버리면 012251 의 형태로 된다.
        # '3'이 있는지 여부
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)
'''