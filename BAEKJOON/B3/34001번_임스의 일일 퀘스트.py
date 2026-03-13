import sys

def solve():
    # 임스의 레벨 입력
    try:
        line = sys.stdin.readline()
        if not line:
            return
        L = int(line.strip())
    except ValueError:
        return

    # 아케인 리버 지역 정보 (퀘스트레벨, 1차 감소, 2차 감소)
    arcane_river = [
        (200, 210, 220), # 소멸의 여로
        (210, 220, 225), # 츄츄 아일랜드
        (220, 225, 230), # 레헬른
        (225, 230, 235), # 아르카나
        (230, 235, 245), # 모라스
        (235, 245, 250)  # 에스페라
    ]

    # 그란디스 지역 정보 (퀘스트레벨, 1차 감소, 2차 감소)
    grandis = [
        (260, 265, 270), # 세르니움
        (265, 270, 275), # 호텔 아르크스
        (270, 275, 280), # 오디움
        (275, 280, 285), # 도원경
        (280, 285, 290), # 아르테리아
        (285, 290, 295), # 카르시온
        (290, 295, 300)  # 탈라하트
    ]

    def get_monster_count(current_level, regions):
        counts = []
        for quest_lv, decrease_1, decrease_2 in regions:
            # 1. 퀘스트 레벨보다 낮으면 수행 불가 (0마리)
            if current_level < quest_lv:
                counts.append(0)
            # 2. 2차 감소 레벨 이상이면 100마리 (500 - 200 - 200)
            elif current_level >= decrease_2:
                counts.append(100)
            # 3. 1차 감소 레벨 이상이면 300마리 (500 - 200)
            elif current_level >= decrease_1:
                counts.append(300)
            # 4. 그 외 수행 가능 레벨이면 기본 500마리
            else:
                counts.append(500)
        return counts

    # 결과 계산
    arcane_results = get_monster_count(L, arcane_river)
    grandis_results = get_monster_count(L, grandis)

    # 출력
    print(*(arcane_results))
    print(*(grandis_results))

if __name__ == "__main__":
    solve()