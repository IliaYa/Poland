'''
def eazy_function():
    a, b, c = map(int, input().split())
    d, e = 0, (a - 1) * max(b, c)
    while e > d + 1:
        f = (e + d) // 2
        if (f // b + f // c) < a - 1:
            d = f
        else:
            e = f
    print(e + min(b, c))


eazy_function()
'''
def binsearchR(x):
    bottom = -1
    top = 10**9
    while bottom + 1 < top:
        center = (top + bottom) // 2
        if printtime(center) >= x:
            top = center
        else:
            bottom = center
    return top

printtime = lambda t: t // x + (t - x) // y

n, x, y = map(int, input().split())
x, y = min(x, y), max(x, y)
print(binsearchR(n))