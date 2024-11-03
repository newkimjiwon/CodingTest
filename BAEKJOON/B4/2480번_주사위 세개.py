a, b, c = map(int ,input().split())

if a == b and b == c and c == a:
    print(10000 + (a * 1000))
elif a != b and b != c and c != a:
    print(max(a, b, c) * 100)
else:
    if a == b and a != c:
        print(1000 + (a * 100))
    elif b == c and b != a:
        print(1000 + (b * 100))
    elif c == a and c != b:
        print(1000 + (c * 100))