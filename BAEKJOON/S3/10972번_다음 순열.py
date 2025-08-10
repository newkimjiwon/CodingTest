import sys


def next_permutation(p):
    """주어진 순열 p의 다음 순열을 찾아주고, 성공하면 True, 실패하면 False를 반환합니다."""
    n = len(p)
    
    # 1. 오른쪽에서부터 왼쪽으로 가며 값이 커지는 지점(i)을 찾는다.
    # 즉, p[i-1] < p[i]를 만족하는 가장 큰 i를 찾는다.
    i = n - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    
    # 만약 i가 0이라면, 전체가 내림차순이므로 마지막 순열이다. (예: 5,4,3,2,1)
    if i <= 0:
        return False
    
    # 2. 다시 오른쪽에서부터 p[i-1]보다 큰 첫 번째 값(p[j])을 찾는다.
    j = n - 1
    while p[j] <= p[i-1]:
        j -= 1
        
    # 3. p[i-1]과 p[j]를 서로 바꾼다.
    p[i-1], p[j] = p[j], p[i-1]
    
    # 4. i부터 끝까지의 부분을 오름차순으로 정렬한다.
    # (이미 내림차순에 가까우므로, 단순히 뒤집어주면 오름차순이 된다.)
    k = n - 1
    while i < k:
        p[i], p[k] = p[k], p[i]
        i += 1
        k -= 1
        
    return True


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    target = list(map(int, sys.stdin.readline().split()))
    
    if next_permutation(target):
        # 리스트의 원소들을 공백으로 구분하여 한 줄에 출력
        print(*target) 
    else:
        # 다음 순열이 없으면 -1을 출력
        print(-1)