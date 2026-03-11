import sys

def solve():
    # 입력을 받습니다.
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        # 도미노 세트의 총 점수 계산 공식
        # 각 숫자 i (0~N)는 전체 세트에서 (N + 2)번 등장합니다.
        # sum = (0 + 1 + ... + N) * (N + 2)
        
        total_sum = (n * (n + 1) // 2) * (n + 2)
        
        print(total_sum)
    except ValueError:
        pass

if __name__ == "__main__":
    solve()