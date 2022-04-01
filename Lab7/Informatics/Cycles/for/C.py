a = int(input())
b = int(input())
for i in range(100000):
    if a <= i * i <= b:
        print(i * i)