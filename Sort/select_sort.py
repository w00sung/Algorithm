
def selection_sort(a):
    n = len(a)
    for i in range(n):
        # 해당 범위에서 가장 맨 앞 idx
        # 가장 앞에 있는 값이 제일 작을수도 있으니까 !!!
        min_idx = i
        for j in range(i,n):
            # idx값만 갖고 비교
            if a[j] < a[min_idx]:
                min_idx = j
            
        a[i],a[min_idx] = a[min_idx],a[i]