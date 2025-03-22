def min_waiting_time(N, T, buses):
    min_wait = float('inf')
    
    for i in range(N):
        Si, Ii, Ci = buses[i]
        
        # 첫 번째 버스부터 마지막 버스까지의 모든 출발 시각 확인
        for j in range(Ci):
            bus_time = Si + j * Ii
            
            # T 이후에 출발하는 가장 빠른 버스 찾기
            if bus_time >= T:
                min_wait = min(min_wait, bus_time - T)
                break  # 이 노선에서 가장 빠른 버스를 찾았으므로 다음 노선으로 이동
    
    if min_wait == float('inf'):
        return -1  # 탈 수 있는 버스가 없음
    else:
        return min_wait

# 입력 처리
N, T = map(int, input().split())
buses = []
for _ in range(N):
    Si, Ii, Ci = map(int, input().split())
    buses.append((Si, Ii, Ci))

# 결과 출력
print(min_waiting_time(N, T, buses))