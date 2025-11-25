def solve():
    x, y = map(int, input().split())
    
    # 버스가 서울대입구역에 도착하는 데 걸리는 총 시간 (주기를 고려하지 않은 단순 합)
    total_time_to_arrive = x + y
    
    # 셔틀버스의 왕복 주기
    cycle_time = 2 * x
    
    # 왕복 주기를 나눈 나머지가 최소 대기 시간
    # (x + y) % (2 * x)
    min_wait_time = total_time_to_arrive % cycle_time
    
    print(min_wait_time)


if __name__ == "__main__":
    solve()