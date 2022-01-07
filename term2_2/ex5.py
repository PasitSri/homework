def tree_sum(arr):
    for i in arr:
        if(not(isinstance(i, int))):
            return -1
    n = len(arr)
    i = 0
    result = []
    arr.sort()
    while(i<n):
        if(i != 0 and arr[i] == arr[i-1]):
            i += 1
            continue
        l, r = i+1, n-1
        while(l<r):
            sum_all = arr[i] + arr[l] + arr[r]
            if (sum_all == 0):
                result.append([arr[i], arr[l], arr[r]])
                while(l<r and arr[l] == arr[l+1]): l += 1
                while(l<r and arr[r] == arr[r-1]): r -= 1
                l += 1
            elif (sum_all > 0):
                r -= 1
            elif (sum_all < 0):
                l += 1
        i += 1
    return result


print(tree_sum([0, -1, 2, -3, 1, -2]))
    

