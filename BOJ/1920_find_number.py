import sys
read = sys.stdin.readline

n = int(read())
find_arr = list(map(int,read().rstrip().split()))

m = int(read())
arr= list(map(int,read().rstrip().split()))


def binary_search(find_arr, find, strt,end):

    while strt <= end:
        mid = (strt + end) // 2

        if find_arr[mid] == find:
            return 1

        elif find_arr[mid] < find:
            strt = mid +1

        else:
            end = mid -1

    return 0



find_arr.sort()

for find in arr:
    print(binary_search(find_arr,find,0,n-1))