def solve():
    if True:
        a = []
        line = input()
        n = int(line.split(' ')[0])
        r = int(line.split(' ')[1])
        line = input()
        for x in line.split(' '):
            a.append(int(x))
    else:
        a = []
        with open("input3.txt") as f:
            for line in f:
                a.append([int(x) for x in line.split()])
        n = a[0][0]
        r = a[0][1]

    b = []
    step = 0
    for x in a:
        step += 1
        if x == 1:
            b.append(step)
    if b == []:
        result = -1
    else:
        if (n <= r) and (b != []):
            result = 1
        else:
            pos = 0
            lastpos = 0
            flag = 0
            shift = r
            i = 1
            result = 0
            left = 0
            right = 0
            while i <= len(b):
                if b[i-1] <= shift:
                    pos = i
                    flag = 1
                    i += 1
                    right = 1
                else:
                    if flag:
                        left = 1
                        right = 0
                        lastpos = pos
                        result += 1
                        shift = b[pos-1] + 2 * r - 1
                        flag = 0
                    else:
                        result = -1
                        flag = 0
                        break
            if flag and (b[lastpos-1] + r - 1 < n):
                result += 1
            if (right == 0) and (b[lastpos-1] + r -1 < n):
                result = -1
    print(result,'\n')

solve()