# 시간복잡도 O(n^2)로 하면 시간초과가 발생한다.
# 시간복잡도를 O(nlogn)으로 줄여야한다.
while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    # 처음에 0을 추가해주는 것은 높이(h)의 인덱스를 1~n까지로 맞춰주기 위함이다.
    # 마지막에 0을 추가해주는 것은 히스토그램 전체의 최소 높이 x 개수를 구하기 위함이다.
    h = [0] + arr[1:] + [0]
    if n == 0:  # 0이 입력되면 종료
        break
    checked = [0]  # 스택의 계산을 원활히 하기 위해 초기값을 하나 준다.
    _max = 0  # 최대 넓이
    # 1~n+1범위로 계산한다.
    # n+1까지 하는 이유는 n+1에서 거슬러 내려오면서 히스토그램 전체의 최소 높이 x 개수를 구하기 위함이다.
    for i in range(1, n+2):
        # 현재(i) 높이보다 아직 확인되지 않은 높이(checked[-1])가 더 클 때,
        while h[checked[-1]] > h[i]:
            # checked.pop() : 아직 확인되지 않은 높이를 확인했다는 뜻
            # 메커니즘상 while 문은 cur_h가 점점 작아지게 된다.
            cur_h = h[checked.pop()]
            # i-1-checked[-1] : 확인되지 않은 다음 인덱스까지의 직사각형 개수
            _max = max(_max, (i-1-checked[-1]) * cur_h)
        checked.append(i)
    print(_max)

# 문제 : https://www.acmicpc.net/problem/6549
