if __name__ == "__main__":
    word = input().strip()

    # 다이얼 매핑
    dial = {
        'ABC': 3, 'DEF': 4, 'GHI': 5,
        'JKL': 6, 'MNO': 7, 'PQRS': 8,
        'TUV': 9, 'WXYZ': 10
    }

    total_time = 0
    for ch in word:
        for group, time in dial.items():
            if ch in group:
                total_time += time
                break

    print(total_time)
