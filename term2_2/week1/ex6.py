def cal_ten_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(n):
            sum_all = arr[i][j]
            if sum_all == 10:
                result += 1
            for k in range(j+1, n):
                sum_all += arr[i][k]
                if sum_all == 10:
                    result += 1
    for i in range(n):
        for j in range(n):
            sum_all = arr[j][i]
            if sum_all == 10:
                result += 1
            for k in range(j+1, n):
                sum_all += arr[k][i]
                if sum_all == 10:
                    result += 1
    return result

def ten_sum():
    n = int(input())
    result = []
    for i in range(n):
        scale = int(input())
        l = []
        for j in range(scale):
            l.append([int(k) for k in input().split()])
        result.append(cal_ten_sum(l))
    print("\n\n")
    for i in result:
        print(i)

ten_sum()


