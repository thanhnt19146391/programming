def solve():
    new_s = ''
    cnt = 0
    if s[0] == '_':
        new_s = '^'
        cnt = 1

    for i in range(len(s)):
        if s[i] == '^':
            cnt += 1
        if len(new_s):
            if new_s[-1] == '_' and s[i] != '^':
                new_s += '^'
        new_s += s[i]
    
    if new_s[-1] == '_' or cnt < 2:
        new_s += '^'
    

    # print(new_s)
    print(len(new_s) - len(s))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve()