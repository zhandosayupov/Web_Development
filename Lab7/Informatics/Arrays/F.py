input()
a = list(map(int, input().split()))
print(sum([1 if a[i - 1] < a[i] > a[i + 1] else 0 for i in range(1, len(a) - 1)]))