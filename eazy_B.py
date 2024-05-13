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
