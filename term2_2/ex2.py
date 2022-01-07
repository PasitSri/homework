def find_plane(n):
    if not isinstance(n, int): return -1
    if n==1: return 2
    if n<1: return 1
    return n + find_plane(n-1)

print(find_plane(5))
    
