import sys

def input():
    return sys.stdin.readline()

n = int(input())

lis = [0] * 10001

for _ in range(n):
    i = int(input())
    lis[i] += 1

for i in range(10001):
    if lis[i] != 0:
        for _ in range(lis[i]):
            print(i)