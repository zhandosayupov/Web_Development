n = int(input())
a = int(input())
if (abs(n - int((str(n)[::-1] + "0000")[:4])) + 1) == 1:
    print("YES" if a == 1 else "NO")
else:
    print("YES" if a != 1 else "NO")