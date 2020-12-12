import sys
read = sys.stdin.readline

n = int(read())

def factorial(n):
    # 마지막은 1로 마무리
    # 0 팩토리얼은 1이다.
    if n in [0,1]:
        return 1

    # 호출할 부분 : [  ]
    # n ! = [n *] [(n-1) *] ... * 1
    else:
        return n * factorial(n-1)

print(factorial(n)) 