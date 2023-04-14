#  https://codeforces.com/contest/1816/problem/A

def solve():
    print(f'2\n{1} {b - 1}\n{a} {b}')


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    solve()
