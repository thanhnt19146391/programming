from array import array

def solve():
 
    res = [array('i', [0] * (n + 1)) for _ in range(3)]

    res[1][1] = 2 * n - 1
    res[2][n] = 2 * n

    for i in range(2, n + 1):
        if i % 2 == 0:
            res[1][i] = i
            res[2][i - 1] = i - 1
        else:
            res[1][i] = n + (i - 1) 
            res[2][i - 1] = n + (i - 1) - 1
    
    for i in range(1, 3):
        for j in range(1, n + 1):
            print(res[i][j], end = '')     
            if j == n:
                print()
            else:
                print(' ', end = '')
    
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        solve()