def duplicate_el(arr):
    for i in arr:
        if(not(isinstance(i, int))):
            return -1
    n = len(arr)
    duplicate_num = []
    for i in range(n-1):
        j = i+1
        for j in range(i+1, n+1):
            if(arr[i] == arr[j] and not (arr[i] in duplicate_num)):
                duplicate_num.append(arr[i])
                break
    return duplicate_num

print(duplicate_el([2,2,3,1,2,3,3,4,4]))
