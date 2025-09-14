import sys
sys.setrecursionlimit(10**6)

visited = set()

def dfs(s, t):
    # 가지치기: t가 s보다 짧아지면 불가능
    if len(t) < len(s):
        return False
    # 길이가 같아지면 일치 여부로 결정
    if len(t) == len(s):
        return s == t

    # 중복 탐색 방지
    if t in visited:
        return False
    visited.add(t)

    # for i in range(2) 분기
    for i in range(2):
        if i == 0:
            # 역연산 1: 끝이 'A'면 마지막 'A' 제거
            if t and t[-1] == 'A':
                if dfs(s, t[:-1]):
                    return True
        elif i == 1:
            # 역연산 2: 시작이 'B'면 첫 글자 'B' 제거 후 뒤집기
            if t and t[0] == 'B':
                if dfs(s, t[1:][::-1]):
                    return True

    return False

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    print(1 if dfs(S, T) else 0)