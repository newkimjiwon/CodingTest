N = int(input())

nlist = list(map(int, input().split()))

ndic = {}

M = int(input())

mlist = list(map(int, input().split()))

for num in nlist:
    if num not in ndic:
        ndic[num] = 1

for num in mlist:
    if num in ndic:
        print(1)
    else:
        print(0)