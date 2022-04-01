n = int(input())
t = 540 + 45 * n + (n - 1) // 2 * 15 + n // 2 * 5
print(t // 60, t % 60)