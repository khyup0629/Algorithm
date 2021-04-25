# 두 소스 모두 메모리와 시간이 같게 나왔음.
# (첫 번째 소스) 현재 알파벳과 뒤의 알파벳이 다를 때 현재 알파벳이 뒤의 알파벳 중에 있다면 그룹 단어가 아니다.
# (두 번째 소스) 알파벳에 대한 방문 여부 리스트를 26개 만들고 첫 방문이 아닌 두 번째 방문이라면 그룹 단어가 아니다.

n = int(input())

cnt = 0
for _ in range(n):
    sentence = input()
    changed = 0  # 그룹 단어임을 나타냄
    for i in range(len(sentence)-1):
        # 현재 알파벳과 뒤의 알파벳이 다르면
        if sentence[i] != sentence[i+1]:
            # 현재 알파벳의 바로 뒤의 알파벳부터 끝까지 문자열 생성
            new_sentence = sentence[i+1:]
            # 바로 뒤의 알파벳부터 끝까지 중에 현재 알파벳이 있다면
            if new_sentence.count(sentence[i]) >= 1:
                changed = 1  # 그룹 단어가 아님을 나타냄
                break
    if changed == 0:  # 그룹 단어라면 카운트 +1
        cnt += 1
print(cnt)

"""
n = int(input())
cnt = 0
for _ in range(n):
    sentence = input()
    # 방문 여부
    visited = [False] * 26  # 알파벳 개수
    # 초기값
    alphabet = sentence[0]  # 앞에 나온 알파벳 임시 저장소
    visited[ord(alphabet)-97] = True
    changed = 0  # 그룹 단어임을 나타냄

    for word in sentence[1:]:
        if alphabet == word:
            continue
        # 이미 방문한 알파벳이라면 반복 종료
        if visited[ord(word)-97]:
            changed = 1  # 그룹 단어가 아님을 나타냄
            break
        alphabet = word  # 다음 나올 알파벳과 같은지를 체크하기 위해
        visited[ord(alphabet) - 97] = True  # 방문 완료

    if changed == 0:  # 만약 그룹 단어라면 카운트 +1
        cnt += 1

print(cnt)
"""