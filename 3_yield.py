def factorize(x: int):
    d = 2
    while x != 1:
        if x % d == 0:
            print('Hello')
            yield d
            x //= d
        else:
            d += 1

A = factorize(1023)
print(A)
for x in map(str, A):
    print('Factor:', x)