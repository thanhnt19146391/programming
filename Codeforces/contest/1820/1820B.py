import math

def solve():
    global s
    n = len(s)
    k = cnt = 0
    s += s
    
    for c in s:
        cnt = cnt + 1 if c == '1' else 0
        k = max(k, cnt)

    if k > n:
        print(n * n)
    else:
        a = math.floor((k + 1) / 2)
        b = math.ceil((k + 1) / 2)
        print(a * b)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        s = input()
        solve()
