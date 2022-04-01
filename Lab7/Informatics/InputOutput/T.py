x = input()
print(abs(int(x) - int((x[::-1] + "0000")[:4])) + 1)