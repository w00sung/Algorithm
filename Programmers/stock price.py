import sys
read = sys.stdin.readline

def solution(prices):
    answer = [0] * len(prices)
    stock = []
    idx = []
    for i in range(len(prices)):
        cnt = 0
        # stock이 있고, 가격이 낮아지는 순간 뽑는다.
        while stock and prices[i] < stock[-1] : 
            stock.pop()
            cnt += 1

        stock.append(prices[i])

        while cnt != 0 and idx:
            cnt -= 1
            j = idx.pop()
            answer[j] = i - j

        idx.append(i)

    while idx:
        j = idx.pop()
        answer [j] = (len(prices)-1)-j
    
    ########### 시간초과 #######################
        # if i == len(prices)-1:
        #     for j in range(i-1, -1, -1):
        #         if answer[j] == 0:
        #             answer[j] = i - j

        # else:    
        #     for j in range(i-1,-1,-1):
        #         if cnt > 0 and answer[j] == 0:
        #             cnt -= 1
        #             answer[j] = i - j
    return answer

    print(stock)
    print(answer)

prices = [1,2,3,2,3]
# prices = [10,20,15,5,30,15]
solution(prices)

        
