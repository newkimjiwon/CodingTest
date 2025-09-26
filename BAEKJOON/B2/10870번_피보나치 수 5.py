def fi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >= 3:
        return fi(n - 1) + fi(n - 2)
    
n = int(input())

print(fi(n))