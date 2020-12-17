import sys
read = sys.stdin.readline

n = int(read())
stuff = []
stuff = list(map(int,read().rstrip().split()))

k = int(read())
find = []
find = list(map(int,read().rstrip().split()))



def binary_search(stuff, target, strt, end):
    while strt <= end:
        
        mid = (strt + end) // 2
        
        if stuff[mid] == target:
            return "yes"

        elif stuff[mid] < target:
            
            strt = mid+1

        else:
            end = mid-1
    return "no"

stuff.sort()
for target in find:
    print(binary_search(stuff,target,0,n-1),end = " ")