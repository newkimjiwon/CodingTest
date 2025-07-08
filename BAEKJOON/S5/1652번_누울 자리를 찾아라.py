def main():
    n = int(input())

    room_map = []
    for _ in range(n):
        row_chars = list(input())
        room_map.append(row_chars)

    horizontal_spots = 0
    vertical_spots = 0

    # 가로 누울 자리 찾기
    for r in range(n):
        current_row_string = "".join(room_map[r])
        parts = current_row_string.split('X')
        
        for part in parts:
            if len(part) >= 2:
                horizontal_spots += 1

    # 세로 누울 자리 찾기
    for c in range(n):
        current_col_string = ""
        for r in range(n):
            current_col_string += room_map[r][c]
        
        parts = current_col_string.split('X')
        
        for part in parts:
            if len(part) >= 2:
                vertical_spots += 1

    print(horizontal_spots, vertical_spots)


if __name__=="__main__":
    main()