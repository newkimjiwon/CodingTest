import math


def solution(g):
    possible_p_values = [] # 가능한 현재 몸무게 P 값을 저장할 리스트

    # (P - M)을 factor2, (P + M)을 factor1이라고 할 때
    # factor1 * factor2 = G
    # P = (factor1 + factor2) / 2
    # M = (factor1 - factor2) / 2

    # factor2 (P - M)는 G의 약수이며, P - M은 1부터 시작할 수 있습니다.
    for factor2 in range(1, int(math.sqrt(g)) + 1):
        # factor2가 G의 약수인지 확인
        if g % factor2 == 0:
            factor1 = g // factor2 # factor1 (P + M) 계산

            # P와 M이 모두 자연수이려면,
            # (factor1 + factor2)와 (factor1 - factor2)가 모두 짝수여야 합니다.
            # 이는 factor1과 factor2의 홀짝성이 같아야 함을 의미합니다.
            if (factor1 + factor2) % 2 == 0:
                P = (factor1 + factor2) // 2
                M = (factor1 - factor2) // 2

                # M이 자연수 (0보다 큼)인지 확인
                # P는 M보다 항상 크므로 (P - M = factor2 > 0), 이 조건만 확인하면 충분합니다.
                if M > 0:
                    possible_p_values.append(P)

    # 가능한 P 값이 없으면 -1 출력
    if not possible_p_values:
        return [-1] # 리스트 형태로 반환하여 main에서 처리 용이하게

    # P 값들을 오름차순으로 정렬
    possible_p_values.sort()
    
    return possible_p_values # 계산된 P 값 리스트 반환


def main():
    g = int(input()) # 몸무게 G 입력

    results = solution(g) # solution 함수 호출

    # 결과 출력
    for weight_val in results:
        print(weight_val)


if __name__=="__main__":
    main()