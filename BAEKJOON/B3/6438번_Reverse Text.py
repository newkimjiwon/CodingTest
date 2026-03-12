import sys

def solve():
    # 첫 번째 줄에서 테스트 케이스의 개수를 읽어옵니다.
    line = sys.stdin.readline()
    if not line:
        return
    
    num_test_cases = int(line.strip())

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        # 한 줄의 텍스트를 읽어옵니다.
        text = sys.stdin.readline().rstrip('\n')
        
        # 문자열을 뒤집어서 출력합니다.
        print(text[::-1])

if __name__ == "__main__":
    solve()