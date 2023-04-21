from array import array

def solve():
    l = 0
    r = n + 1
    while (l + 1 <= n):
        l += 1
        if _a[l] != a[l]:
            break
            
    while (r - 1 >= 0):
        r -= 1
        if _a[r] != a[r]:
            break
    
    while (l - 1 >= 1):
        if _a[l - 1] <= _a[l]:
            l -= 1
        else:
            break
    
    while (r + 1 <= n):
        if _a[r + 1] >= _a[r]:
            r += 1
        else:
            break

    if (l <= r):
        print(f'{l} {r}')
        return

    b = array('i', [0] * n)
    len_max = 0
    len = 0
    res_l = 1
    res_r = 1
    for i in range(1, n):
        b[i] = _a[i + 1] - _a[i]
        if b[i] >= 0:
            if len == 0:
                l = i
            len += 1
        else:
            len = 0
        
        if len > len_max:
            len_max = len
            res_l = l
            res_r = l + len_max

    # print(_a)
    # print(b)
    print(f'{res_l} {res_r}')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = array('i', [int(x) for x in input().split()])
        _a = array('i', [int(x) for x in input().split()])
        a.insert(0, 0)
        _a.insert(0, 0)
        solve()

""" 
6
7
6 7 3 4 4 6 5
6 7 3 4 4 6 5
5
2 2 2 2 2
2 2 2 2 2 
5
5 4 3 2 1
1 2 3 4 5
5
5 4 3 2 1
5 4 3 2 1
5
5 4 3 2 1
5 4 2 3 1
5
5 4 3 2 1
5 4 3 1 2
 """