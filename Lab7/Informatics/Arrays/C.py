input()
print(sum([1 if x > 0 else 0 for x in list(map(int, input().split()))]))