import sys
read = sys.stdin.readline

def merge_sort(uns_list):

    if len(uns_list) <= 1:
        return uns_list
    
    center = len(uns_list)//2
    left = uns_list[:center]

    right = uns_list[center:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list,right_list)


def merge(left, right):

    i = 0
    j = 0
    srt_list = []

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            srt_list.append(left[i])
            i += 1

        else:
            srt_list.append(right[j])
            j+=1

    while (i < len(left)):
        srt_list.append(left[i])
        i += 1

    
    while (j < len(right)):
        srt_list.append(right[j])
        j += 1

    return srt_list

n = int(read())
li = []
for _ in range(n):
    li.append(int(read()))
    
print("\n".join([str(k) for k in merge_sort(li)]))



    
