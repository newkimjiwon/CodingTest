import sys

def solve():
    # 1. 알파벳별 숫자 매핑 딕셔너리 생성
    keypad = {}
    for char in "ABC": keypad[char] = "2"
    for char in "DEF": keypad[char] = "3"
    for char in "GHI": keypad[char] = "4"
    for char in "JKL": keypad[char] = "5"
    for char in "MNO": keypad[char] = "6"
    for char in "PQRS": keypad[char] = "7"
    for char in "TUV": keypad[char] = "8"
    for char in "WXYZ": keypad[char] = "9"

    # 2. 입력 받기
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    for _ in range(n):
        company_name = sys.stdin.readline().strip().upper()
        if not company_name:
            continue
            
        # 3. 이름을 숫자 문자열로 변환
        phone_number = ""
        for char in company_name:
            if char in keypad:
                phone_number += keypad[char]
        
        # 4. 회문(Palindrome) 검사
        # [::-1]은 문자열을 뒤집는 파이썬의 슬라이싱 기법입니다.
        if phone_number == phone_number[::-1]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()