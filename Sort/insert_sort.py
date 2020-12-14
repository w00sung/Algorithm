def insertion_sort(a):
    n = len(a)
    # i 는 정렬되지 않은 가장 첫 원소
    # 앞부분 부터 차곡차곡 정렬하기 때문에 i를 1씩 늘린다!!
    for i in range(1,n):
        print("정렬되지 않은 부분의 시작 :", i)
        tmp = a[i]
        print ("지금 tmp : ",tmp) 
        # j는 앞의 놈들 당길 인덱스
        j = i
        while True:
            print("현재 탐색 중인 j :", j)  
            print(" tmp : {} vs a[j-1] : {}".format(tmp,a[j-1]))
            if tmp >= a[j-1] or j == 0:
                print("지금의 tmp ", tmp)
                # 작은 것 만나면 놓고 out !
                # 앞에 놈이 나보다 작거나 같으면
                # or 내가 맨 앞이면
                a[j] = tmp
                print("앞부분 보다 작거나, 끝까지 왔다",a)
                break
            # 작은 것 안만났으면,
            a[j] = a[j-1]
            j -= 1
            print("앞부분 보다 커서 저장",a)
            print("j를 줄입니다",j)

a = [4,6,1,7,3]

print(insertion_sort(a))


