from array import array

def solve():
    res = 1
    if n == 2:
        if a[0] > a[1]:
            res = 0
    else:
        for i in range(n - 2):
            if a[i] > a[i + 1] and a[i + 1] < a[i + 2]:
                res = 0
                
    print('YES' if res else 'NO')

        

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = array('i', [int(x) for x in input().split()])
        solve()
