from bisect import bisect as upper_bound  
def countPairs(a, n, mid):  
    res = 0
    for i in range(n):  
        res += upper_bound(a, a[i] + mid)  
    return res  

def kthDiff(a, n, k):  
    a = sorted(a)  
    low = a[1] - a[0]  
    for i in range(1, n - 1):  
        low = min(low, a[i + 1] - a[i])  
    high = a[n - 1] - a[0]  

    while (low < high):  
        mid = (low + high) >> 1
        if (countPairs(a, n, mid) < k):  
            low = mid + 1
        else:  
            high = mid  
    return low  

k = 3
a = [1, 2, 3, 4]  
n = len(a)  
print(kthDiff(a, n, k)) 