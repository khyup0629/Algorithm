# 문자열의 양끝에서 가운데로 오면서 하나씩 철자가 같은지 비교하면 된다.
sentence = input()

same = True
for i in range(len(sentence)//2):
    if sentence[i] != sentence[-i-1]:
        same = False
        break

print(1 if same else 0)

"""
문제
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

예제 입력 1 
level
예제 출력 1 
1
예제 입력 2 
baekjoon
예제 출력 2 
0
"""