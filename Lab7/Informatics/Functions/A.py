def min(a, b, c, d):
    x = 1e18
    if a < x:
        x = a
    if b < x:
        x = b
    if c < x:
        x = c
    if d < x:
        x = d
    return x


a, b, c, d = list(map(int, input().split()))
print(min(a, b, c, d))