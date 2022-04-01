def power(a, b):
    return pow(a, b)


a, n = list(map(int, input().split()))
print(power(a, n))