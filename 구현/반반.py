T = int(input())
for test_case in range(1, T + 1):
    string = input()
    dic = {}
    lst = []
    for word in string:
        dic[word] = dic.get(word, 0) + 1

    changed = False
    for word in dic:
        if len(dic) != 2 or dic[word] != 2:
            changed = True

    if not changed:
        print('#', test_case, ' Yes', sep='')
    else:
        print('#', test_case, ' No', sep='')

# 문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXjS1GXqZ8gDFATi
