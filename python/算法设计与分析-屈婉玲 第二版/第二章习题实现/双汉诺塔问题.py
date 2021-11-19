def DoubleHanoi(n, A, B, C):
    if n == 1:
        print(A, '->', C)
        print(A, '->', C)
        return
    DoubleHanoi(n-1, A, C, B)
    print(A, '->', C)
    print(A, '->', C)
    DoubleHanoi(n-1, B, A, C)


m = eval(input())
DoubleHanoi(m//2, 'A', 'B', 'C')
