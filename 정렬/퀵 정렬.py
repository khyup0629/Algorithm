# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫 번째 데이터를 피벗값으로 설정한 후
# 왼쪽에서부터 피벗값보다 큰 첫 번째 데이터,
# 오른쪽에서부터 피벗값보다 첫 번째 작은 데이터를 선택
# 두 위치를 변경
# 위치가 엇갈린다면 작은 데이터와 피벗값의 위치를 변경
# 이렇게 되면 피벗값을 기준으로 작은 데이터와 큰 데이터가 나뉜다(분할)
# 피벗값을 제외한 두 데이터 묶음에 대하여 퀵 정렬, 재귀 함수

# start : 시작 인덱스, end : 끝 인덱스
def quick_sort(array, start, end):
    # 재귀 함수 quick_sort 의 종료 조건
    # 원소가 1개인 경우 종료, start >= end 일 때 항상 원소가 1개
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # 큰 데이터와 작은 데이터의 인덱스가 서로 엇갈리면 반복 종료
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        # 전체 배열 범위를 벗어났거나 피벗값보다 큰 값을 찾으면 반복 종료
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        # 피벗값이 최솟값이 되면 right = start 가 된다
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 큰 데이터와 작은 데이터의 인덱스가 서로 엇갈렸다면
        if left > right:
            # 스왑 후 분할, 엇갈린 이후에는 right 이 피벗값이 위치한 인덱스가 됨.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 작은 데이터와 큰 데이터 스왑
            array[left], array[right] = array[right], array[left]
    # 피벗값을 제외한 앞/뒤 데이터 묶음에 대해 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)