input()
a = list(map(int, input().split()))
print(sum([1 if a[i + 1] > a[i] else 0 for i in range(len(a) - 1)]))