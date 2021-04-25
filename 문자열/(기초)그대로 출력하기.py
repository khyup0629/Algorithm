# 기약없는 입력을 반복적으로 받아야 할 때
# EOFError 는 입력을 받는 도중에 Ctrl+d에 의해
# 파일의 끝에 도달하게 될 경우 뜨는 에러
# 따라서 입력을 무한정 받다가 종료하고 싶을 때 Ctrl+d를 누르면
# EOFError 에러가 뜨고 이를 이용해 반복을 종료하는 방법

while True:
    try:
        print(input())
    except EOFError:  # EOF(End Of File)/Error
        break

print('x')
# 마지막에 print('x')를 넣고 실험해보면
# 입력을 계속 받다가 중간에 Ctrl + d를 누르게 되면
# EOFError 가 발생하고 이때 except 에 의해
# 입력 반복문을 빠져나옴으로써
# 맨 끝에 'x'가 출력되는 것을 알 수 있다.
