def solve():
    line = input()
    q = int(line.split(' ')[0])
    i = 1
    sum = []
    while i <= q:
        line = input()
        l = int(line.split(' ')[0])
        r = int(line.split(' ')[1])
        a = ((r -l + 1) // 2)*pow(-1,l+1)
        b = ((r - l + 1) % 2)*r*pow(-1,r)
        sum.append(a+b)
        i += 1
    i = 1
    while i <= q:
        print(sum[i-1])
        i += 1

solve()