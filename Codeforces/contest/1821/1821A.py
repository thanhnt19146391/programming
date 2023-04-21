def solve():
    if s[0] == '0':
        print(0)
        return
    res = 0
    for i in range(len(s)):
        if s[i] == '?':
            if res == 0:
                res = 1
            if i == 0:
                res *= 9
            else:
                res *= 10
    if res == 0: # no question mark
        res = 1
    print(res)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve()
    