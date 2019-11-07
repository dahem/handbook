MOD = 10**9 + 7


def binpow(a, b, mod):
    a %= mod
    res = 1
    while(b > 0):
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res


a, b, k, c = map(int, input().split())

if c != a and c != b:
    print(0)
    exit()

if a == b:
    print(k)
    exit()

print(binpow(2, k-1, MOD) * k % MOD)
