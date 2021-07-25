# 핵심 아이디어
# 1. swap 횟수 = 현재 원소를 기준으로 오른쪽에 있는 작은 원소의 개수
# 2. 왼쪽 묶음과 오른쪽 묶음으로 분할해가며 작은 단위부터 거슬러 올라오면서 재귀적으로 구한다.
# 3. new_arr를 두고 현재 묶음에서 새로 정렬된 원소를 차례대로 추가한 뒤 arr에 갱신한다.
# 4. 왼쪽 묶음의 원소가 new_arr에 추가될 때 오른쪽 묶음의 원소 중 현재 왼쪽 묶음의 원소보다 작은 원소의 개수만큼 swap 횟수를 추가한다.
import sys
sys.setrecursionlimit(10**5)
n = int(input())
arr = list(map(int, input().split()))
swap = 0


def merge_sort(start, end):
    global swap
    mid = (start + end) // 2
    if end - start <= 1:  # 범위 내에 원소가 1개만 존재한다면 스킵
        return

    merge_sort(start, mid)
    merge_sort(mid, end)

    new_arr = []  # 현재 묶음에서 정렬된 원소가 순서대로 저장될 임시 저장소
    # 왼쪽과 오른쪽의 첫 번째 인덱스
    idx1, idx2 = start, mid
    cnt = 0  # 왼쪽 원소를 new_arr에 추가할 때 그 원소보다 작은 오른쪽 원소의 개수를 의미.
    # 왼쪽 묶음과 오른쪽 묶음의 원소를 하나씩 비교하며 new_arr에 순서대로 오름차순 정렬하며 추가한다.
    while idx1 < mid and idx2 < end:
        if arr[idx1] > arr[idx2]:
            new_arr.append(arr[idx2])
            idx2 += 1  # 오른쪽의 다음 원소
            cnt += 1  # 왼쪽 원소를 new_arr에 추가할 때 왼쪽 원소보다 작은 오른쪽 원소의 개수를 의미
        else:
            new_arr.append(arr[idx1])
            idx1 += 1
            swap += cnt  # 오른쪽 묶음의 arr[idx1]보다 작은 원소의 개수만큼 더한다.

    # 남은 왼쪽 묶음의 원소들을 new_arr에 추가한다.
    while idx1 < mid:
        new_arr.append(arr[idx1])
        idx1 += 1
        swap += cnt  # 오른쪽 묶음의 arr[idx1]보다 작은 원소의 개수만큼 더한다.

    # 바뀐 부분만 arr에 갱신한다.
    for i in range(len(new_arr)):
        arr[start+i] = new_arr[i]


merge_sort(0, n)
print(swap)

# 문제 : https://www.acmicpc.net/problem/1517


# 처음부터 시간을 줄였다고 생각한 코드였으나 시간 초과
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
cnt = 0
k = 0
while True:
    k += 1
    if k % 2 == 1:
        for i in range(1, n, 2):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                cnt += 1
    else:
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                cnt += 1
    if sorted_arr == arr:
        print(cnt)
        break
