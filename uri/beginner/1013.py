a, b, c = map(float, input().split())


def mai(a, b):
    return (a+b+abs(a-b)) // 2


print(int(mai(mai(a, b), c)), 'eh o maior')
