import sys

if __name__ == "__main__":
    # 직원의 수
    n = int(sys.stdin.readline().strip())

    employee = {}  # 회사원 상태를 저장하는 딕셔너리

    for _ in range(n):
        name, state = sys.stdin.readline().split()  # 이름과 상태 입력 받기
        if state == 'enter':  
            employee[name] = 1  # 입장하면 1로 표시
        else:  # leave인 경우
            employee[name] = 0  # 퇴장하면 0으로 표시

    enter_member = [name for name, status in employee.items() if status == 1]  # 남아 있는 사람 필터링
    enter_member.sort(reverse=True)  # 이름 기준으로 역순 정렬

    print("\n".join(enter_member))  # 한 번에 출력