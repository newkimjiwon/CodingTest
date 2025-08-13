import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve():
    N = int(sys.stdin.readline())
    trees = [int(sys.stdin.readline()) for _ in range(N)]
    
    # 1. 모든 간격 계산
    intervals = []
    for i in range(1, N):
        intervals.append(trees[i] - trees[i - 1])
    
    # 2. 모든 간격들의 최대공약수(GCD) 계산
    # 첫 번째 간격을 기준으로 시작
    final_interval = intervals[0]
    for i in range(1, len(intervals)):
        final_interval = gcd(final_interval, intervals[i])
        
    # 3. 심어야 할 나무의 총 개수 계산
    total_new_trees = 0
    for interval in intervals:
        total_new_trees += (interval // final_interval) - 1
        
    print(total_new_trees)

solve()