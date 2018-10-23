def solve():
    line = input()
    a = int(line.split(' ')[0])
    b = int(line.split(' ')[1])
    c = int(line.split(' ')[2])
    rslt = 0
    if a >= b + c:
        rslt = a - b - c + 1
    if b >= a + c:
        rslt = b - a - c + 1
    if c >= a + b:
        rslt = c - a - b + 1
    print(rslt)

solve()
