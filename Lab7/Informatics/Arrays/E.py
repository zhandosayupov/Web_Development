input()
a = list(map(int, input().split()))
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > 0:
        print("YES")
        exit(0)
print("NO")