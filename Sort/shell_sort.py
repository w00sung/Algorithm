import sys
read =sys.stdin.readline

def shell_sort(a):
    n = len(a)
    h = n // 2 # 절반 값 부터 시작
    while True:
        if h == 0 :
            break
        # range(h,n) : 절반 이후 값들만 tmp로!
        for i in range(h,n):
            j = i - h
            # print("살펴볼 index", j)
            # 절반 이후 값들을 tmp로
            tmp = a[i]
            # print ("tmp {} vs a[j] {}".format(tmp,a[j]),"현재 a", a)
            while True:
                if tmp >= a[j] or j < 0:
                    # j는 비교 대상의 위치다 ! 
                    # 내가 있어야할 위치는 j+h
                    a[j+h] = tmp
                    # print("내 위치 찾았다 !", a)
                    break
                # 내가 더 작으면
                a[j+h] = a[j]
                j -= h
                # print("뒤로 밀기",a)
        h //= 2
        # print("h변경 ",h)
    return(a)


# a = [4,6,1,7,3]
n = int(read())
li = []
for _ in range(n):
    li.append(int(read()))

print("\n".join([str(k) for k in shell_sort(li)]))

                
