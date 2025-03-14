def solution(players, m, k):
    # server[i]는 i시부터 해당 시간대에 이미 운영 중인 증설 서버 수를 나타냅니다.
    server = [0] * len(players)
    server_cnt = 0  # 하루 동안 증설한 서버 총 횟수

    for i in range(len(players)):
        # 만약 해당 시간대의 이용자가 m명 이상이면 증설 대상
        if players[i] >= m:
            # [n*m, (n+1)*m) 구간에 해당하면 최소 n대의 서버가 필요함.
            # 여기서 n은 floor division으로 구합니다.
            required = players[i] // m   # 필요한 서버 수 n

            # 이미 할당된 서버(server[i])와 비교해서 부족한 서버가 있다면
            if server[i] < required:
                additional = required - server[i]  # 추가로 증설해야 할 서버 수

                # (required * m) <= players[i] < ((required+1) * m) 조건은 항상 만족하므로 그대로 진행
                server_cnt += additional

                # 추가 증설한 서버는 k시간 동안 유지되므로, i시부터 i+k-1시까지 서버 수를 갱신
                for j in range(k):
                    if i + j < len(server):
                        server[i + j] += additional
                    else:
                        break

    return server_cnt
