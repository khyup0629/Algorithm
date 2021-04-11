result = []
for i in range(1, 10000+1):
    result.append(i)

for i in range(1, 10000+1):
    # 생성자가 있는 수 구하기
    element = list(str(i))
    hap = i
    for j in element:
        hap += int(j)
    # 생성자가 있는 수를 리스트에서 지우면 생성자가 없는 수만 남는다
    if result.count(hap) == 1:
        result.remove(hap)

for i in result:
    print(i)

"""
입력 예시

출력 예시
1
3
5
7
9
20
31
42
53
64
 |
 |       <-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
"""