def solve():
    sample = 'Datalogic'

    k = len(sample)
    res = ''
    i = 0
    while (i < len(s)):
        # print(s[i: i + k])
        if s[i : i + k] == sample:
            res += sample
            i += k
        else:
            res += '*'
            i += 1
    print(res)

if __name__ == '__main__':
    s = input()
    solve()
    

    

# 12wsedrData2fsdflofdtalogi3dafgnepDatalogic4235logicg2ekd
# DataloDatalogicDatagicloDatalogic