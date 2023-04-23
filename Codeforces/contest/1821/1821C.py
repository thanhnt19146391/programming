from collections import deque

def check(s):
    ck = 1
    for i in range(1, len(s)):
        if s[i] != s[0]:
            ck = 0
            break
    return ck

def bfs(start):
    queue = deque([(start, 0)])

    while queue:
        vertex, cnt = queue.popleft()
        if check(vertex):
            res = cnt
            break
        if len(vertex) > 1:
            s1 = ''.join(vertex[i] for i in range(0, len(vertex), 2))
            s2 = ''.join(vertex[i] for i in range(1, len(vertex), 2))
            queue.extend([(s1, cnt + 1), [s2, cnt + 1]])
        
    print(res)

def solve():
    _s = s[0]
    for i in range(1, len(s)):
        if s[i] != _s[len(_s) - 1]:
            _s += s[i]
    # print(_s)
    bfs(_s)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve()