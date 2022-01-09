def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def duplicate_el(arr):
    for i in arr:
        if(not(isinstance(i, int))):
            return -1
    n = len(arr)
    duplicate_num = []
    arr = sort(arr)
    for i in range(n-1):
        if(i>0 and arr[i] == arr[i-1]):
          continue
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                duplicate_num.append(arr[i])
                break
    return duplicate_num

print(duplicate_el([2,2,3,1,2,3,3,4,4]))
