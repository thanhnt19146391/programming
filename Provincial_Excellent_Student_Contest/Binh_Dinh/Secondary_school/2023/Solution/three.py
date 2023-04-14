from array import array
import math

def solve():
    a = array('u', sorted(s))
    count = array('i', [])
    pos = array('i', [])
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a):
            if a[i] == a[j + 1]:
                j += 1
            else:
                break
        pos.append(i)
        count.append(j - i + 1)
        i = j + 1
    
    if len(pos) == 1: 
        subtask = 0
    else: 
        subtask = 1

    res = array('u', [])

    if subtask == 0:
        for _ in range(math.ceil(n / k)):
            res.append(a[0])
            
    if subtask == 1:
        if count[0] < k:
            res.append(a[k-1])
        else:
            if count[0] > k:
                for _ in range(count[0] - k + 1):
                    res.append(a[0])
                for i in range(pos[1], len(a)):
                    res.append(a[i])
            else:   # count[0] == k;
                res.append(a[0])
                i = 0
                while (i + 1 < len(count)):
                    i += 1
                    if count[i] % k == 0:
                        for _ in range(count[i] // k):
                            res.append(a[pos[i]])
                    else: 
                        for j in range(pos[i], len(a)):
                            res.append(a[j])
                        break
            
    # print(pos)                    
    # print(count)
    print(''.join(x for x in res))
        
        
                





if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    solve()

