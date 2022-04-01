n = int(input())
m = int(input())
print(n // m * (n % m) + m // n * (m % n) + 1)