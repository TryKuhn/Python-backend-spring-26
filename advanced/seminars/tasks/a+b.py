a, b = input().split()

try:
    a = int(a)
    b = int(b)
except ValueError:
    pass

print(a + b)
