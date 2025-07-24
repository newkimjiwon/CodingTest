import sys

def solve():
    """
    하나의 테스트 케이스를 해결하는 함수.
    DP를 사용하여 4가지 시나리오별 최소 소대 수를 계산하고, 그중 최솟값을 찾습니다.
    """
    try:
        line = sys.stdin.readline()
        if not line: return False
        n, w = map(int, line.split())
        zone_inner = list(map(int, sys.stdin.readline().split())) # 내부 원 (1 ~ N)
        zone_outer = list(map(int, sys.stdin.readline().split())) # 외부 원 (N+1 ~ 2N)
    except (IOError, ValueError):
        return False

    min_total_teams = float('inf')

    # --- DP 상태 정의 ---
    # dp_full[i]: 0열부터 'i-1'열까지 모두 점령했을 때의 최소 소대 수
    # dp_inner_ahead[i]: 내부 원은 'i'열까지, 외부 원은 'i-1'열까지 점령했을 때의 최소 소대 수
    # dp_outer_ahead[i]: 내부 원은 'i-1'열까지, 외부 원은 'i'열까지 점령했을 때의 최소 소대 수
    # 배열 크기는 N+1로 하여 인덱스를 직관적으로 사용합니다.

    # =================================================================================
    # Case 1: 1열과 N열이 전혀 연결되지 않는 경우 (기본 직선 DP)
    # =================================================================================
    dp_full = [0] * (n + 1)
    dp_inner_ahead = [0] * (n + 1)
    dp_outer_ahead = [0] * (n + 1)

    # 0열에 대한 초기값 설정
    dp_full[0] = 0          # -1열까지 점령하는 비용은 0
    dp_inner_ahead[0] = 1   # 내부 0열만 점령하는 비용은 1
    dp_outer_ahead[0] = 1   # 외부 0열만 점령하는 비용은 1

    # 0열부터 N-1열까지 순차적으로 DP 테이블 채우기
    for i in range(n):
        # 점화식 계산 (i+1 상태를 i 상태로부터 계산)

        # 1. dp_full[i+1] 계산 (i열까지 완전히 점령하는 경우)
        #   - 옵션 1: i열의 내부/외부를 각각 점령 (이전 상태가 dp_inner_ahead[i] 또는 dp_outer_ahead[i])
        #   - 옵션 2: i열을 수직으로 묶어 점령 (이전 상태가 dp_full[i])
        #   - 옵션 3: i-1, i열을 수평으로 묶어 점령 (이전 상태가 dp_full[i-1])
        option1 = min(dp_inner_ahead[i] + 1, dp_outer_ahead[i] + 1)
        option2 = dp_full[i] + 1 if zone_inner[i] + zone_outer[i] <= w else float('inf')
        option3 = dp_full[i-1] + 2 if i > 0 and zone_inner[i-1] + zone_inner[i] <= w and zone_outer[i-1] + zone_outer[i] <= w else float('inf')
        dp_full[i+1] = min(option1, option2, option3)

        if i == n - 1: continue # 마지막 열에서는 다음 상태가 없음

        # 2. dp_inner_ahead[i+1] 계산 (내부 i+1열, 외부 i열까지 점령)
        #   - 옵션 1: i열까지 완전히 점령한 상태에서 내부 i+1열을 추가 점령
        #   - 옵션 2: 외부 i열까지 점령한 상태에서 내부 i, i+1열을 묶어 점령
        option_b1 = dp_full[i+1] + 1
        option_b2 = dp_outer_ahead[i] + 1 if zone_inner[i] + zone_inner[i+1] <= w else float('inf')
        dp_inner_ahead[i+1] = min(option_b1, option_b2)

        # 3. dp_outer_ahead[i+1] 계산 (내부 i열, 외부 i+1열까지 점령)
        #   - 옵션 1: i열까지 완전히 점령한 상태에서 외부 i+1열을 추가 점령
        #   - 옵션 2: 내부 i열까지 점령한 상태에서 외부 i, i+1열을 묶어 점령
        option_c1 = dp_full[i+1] + 1
        option_c2 = dp_inner_ahead[i] + 1 if zone_outer[i] + zone_outer[i+1] <= w else float('inf')
        dp_outer_ahead[i+1] = min(option_c1, option_c2)

    min_total_teams = min(min_total_teams, dp_full[n])

    # =================================================================================
    # Case 2: 내부 원의 0열과 (N-1)열이 연결되는 경우
    # =================================================================================
    if n > 1 and zone_inner[0] + zone_inner[n-1] <= w:
        dp_full = [0] * (n + 1)
        dp_inner_ahead = [0] * (n + 1)
        dp_outer_ahead = [0] * (n + 1)

        # 1열에 대한 초기값 설정 (0열의 내부 구역은 이미 점령되었다고 가정)
        dp_full[1] = 1  # 0열 외부 구역만 점령하는 비용
        dp_inner_ahead[1] = 2 # 0열 외부, 1열 내부를 각각 점령
        dp_outer_ahead[1] = 1 if zone_outer[0] + zone_outer[1] <= w else 2

        # 1열부터 N-1열까지 DP 진행
        for i in range(1, n):
            option1 = min(dp_inner_ahead[i] + 1, dp_outer_ahead[i] + 1)
            option2 = dp_full[i] + 1 if zone_inner[i] + zone_outer[i] <= w else float('inf')
            option3 = dp_full[i-1] + 2 if i > 1 and zone_inner[i-1] + zone_inner[i] <= w and zone_outer[i-1] + zone_outer[i] <= w else float('inf')
            dp_full[i+1] = min(option1, option2, option3)

            if i == n - 1: continue

            option_b1 = dp_full[i+1] + 1
            option_b2 = dp_outer_ahead[i] + 1 if zone_inner[i] + zone_inner[i+1] <= w else float('inf')
            dp_inner_ahead[i+1] = min(option_b1, option_b2)
            
            option_c1 = dp_full[i+1] + 1
            option_c2 = dp_inner_ahead[i] + 1 if zone_outer[i] + zone_outer[i+1] <= w else float('inf')
            dp_outer_ahead[i+1] = min(option_c1, option_c2)

        # 최종 비용: (내부 N-2열, 외부 N-1열까지 점령 비용) + (내부 0, N-1 연결 소대 비용 1)
        min_total_teams = min(min_total_teams, dp_outer_ahead[n-1] + 1)

    # =================================================================================
    # Case 3: 외부 원의 0열과 (N-1)열이 연결되는 경우
    # =================================================================================
    if n > 1 and zone_outer[0] + zone_outer[n-1] <= w:
        dp_full = [0] * (n + 1)
        dp_inner_ahead = [0] * (n + 1)
        dp_outer_ahead = [0] * (n + 1)

        # 1열에 대한 초기값 설정 (0열의 외부 구역은 이미 점령되었다고 가정)
        dp_full[1] = 1
        dp_outer_ahead[1] = 2
        dp_inner_ahead[1] = 1 if zone_inner[0] + zone_inner[1] <= w else 2
        
        # 1열부터 N-1열까지 DP 진행
        for i in range(1, n):
            option1 = min(dp_inner_ahead[i] + 1, dp_outer_ahead[i] + 1)
            option2 = dp_full[i] + 1 if zone_inner[i] + zone_outer[i] <= w else float('inf')
            option3 = dp_full[i-1] + 2 if i > 1 and zone_inner[i-1] + zone_inner[i] <= w and zone_outer[i-1] + zone_outer[i] <= w else float('inf')
            dp_full[i+1] = min(option1, option2, option3)

            if i == n - 1: continue

            option_b1 = dp_full[i+1] + 1
            option_b2 = dp_outer_ahead[i] + 1 if zone_inner[i] + zone_inner[i+1] <= w else float('inf')
            dp_inner_ahead[i+1] = min(option_b1, option_b2)
            
            option_c1 = dp_full[i+1] + 1
            option_c2 = dp_inner_ahead[i] + 1 if zone_outer[i] + zone_outer[i+1] <= w else float('inf')
            dp_outer_ahead[i+1] = min(option_c1, option_c2)

        # 최종 비용: (내부 N-1열, 외부 N-2열까지 점령 비용) + (외부 0, N-1 연결 소대 비용 1)
        min_total_teams = min(min_total_teams, dp_inner_ahead[n-1] + 1)

    # =================================================================================
    # Case 4: 내부와 외부 원 모두 0열과 (N-1)열이 연결되는 경우
    # =================================================================================
    if n > 1 and zone_inner[0] + zone_inner[n-1] <= w and zone_outer[0] + zone_outer[n-1] <= w:
        dp_full = [0] * (n + 1)
        dp_inner_ahead = [0] * (n + 1)
        dp_outer_ahead = [0] * (n + 1)

        # 1열에 대한 초기값 설정 (0열 전체가 이미 점령되었다고 가정)
        dp_full[1] = 0
        dp_inner_ahead[1] = 1
        dp_outer_ahead[1] = 1
        
        # 1열부터 N-2열까지 DP 진행
        for i in range(1, n - 1):
            option1 = min(dp_inner_ahead[i] + 1, dp_outer_ahead[i] + 1)
            option2 = dp_full[i] + 1 if zone_inner[i] + zone_outer[i] <= w else float('inf')
            option3 = dp_full[i-1] + 2 if i > 1 and zone_inner[i-1] + zone_inner[i] <= w and zone_outer[i-1] + zone_outer[i] <= w else float('inf')
            dp_full[i+1] = min(option1, option2, option3)

            if i == n - 2: continue

            option_b1 = dp_full[i+1] + 1
            option_b2 = dp_outer_ahead[i] + 1 if zone_inner[i] + zone_inner[i+1] <= w else float('inf')
            dp_inner_ahead[i+1] = min(option_b1, option_b2)
            
            option_c1 = dp_full[i+1] + 1
            option_c2 = dp_inner_ahead[i] + 1 if zone_outer[i] + zone_outer[i+1] <= w else float('inf')
            dp_outer_ahead[i+1] = min(option_c1, option_c2)
        
        # 최종 비용: (N-2열까지 점령 비용) + (양쪽 연결 소대 비용 2)
        min_total_teams = min(min_total_teams, dp_full[n-1] + 2)

    sys.stdout.write(str(min_total_teams) + '\n')
    return True

def main():
    """
    메인 함수: 테스트 케이스의 수만큼 solve 함수를 반복 호출합니다.
    """
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            if not solve():
                break
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()