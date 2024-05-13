def matrix_sum():
    x, y = map(int, input().split())
    z = [list(map(int, input().split())) for i in range(x)]
    q = [[0] * y for i in range(x)]
    w = [[''] * y for i in range(x)]
    q[0][0] = z[0][0]
    for j in range(1, y):
        q[0][j] = q[0][j - 1] + z[0][j]

    for i in range(1, x):
        q[i][0] = q[i - 1][0] + z[i][0]

    for i in range(1, x):
        for j in range(1, y):
            if q[i][j - 1] > q[i - 1][j]:
                q[i][j] = q[i][j - 1] + z[i][j]
            else:
                q[i][j] = q[i - 1][j] + z[i][j]

    print(q[-1][-1])


matrix_sum()
