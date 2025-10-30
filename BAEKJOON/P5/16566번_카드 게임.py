import sys
# M이 매우 크므로 재귀 깊이 제한을 반드시 풀어야 합니다.
sys.setrecursionlimit(10**6)


def find(u, i):
    # 1. 'i'가 딕셔너리에 없다? -> 사용된 적 없으므로 'i'가 루트.
    if i not in u:
        return i
    
    # 2. 'i'가 딕셔너리에 있다? 
    #    -> 'i'는 사용됐고, u[i]로 가라고 함.
    #    -> u[i]가 가리키는 곳의 '진짜' 루트를 재귀로 찾음.
    root = find(u, u[i])
    
    # 3. 경로 압축 (성능 최적화)
    #    'i'가 '진짜' 루트를 바로 가리키도록 갱신.
    #    (다음에 또 'i'를 찾으면 중간과정 없이 바로 'root'로 감)
    u[i] = root 
    return root


def solution(minsu, charles, N, M, K):
    answer = []

    minsu.sort()  # 정렬된 민수의 카드
    union = {}  # Union-Find

    for k in range(K):
        card_C = charles[k]  # 현재 철수의 카드

        left = 0
        right = M - 1

        while left <= right:
            center = (left + right) // 2 # 중앙값
            card_M = minsu[center]  # 중간에 있는 민수 카드

            if card_C < card_M : # 중간에 있는 민수의 카드가 철수의 카드보다 크면
                right = center - 1
            elif card_C >= card_M: # 중간에 있는 민수의 카드가 철수의 카드보다 크면
                left = center + 1
        
        actual_idx = find(union, left)
        answer.append(minsu[actual_idx])
        union[actual_idx] = actual_idx + 1

    return answer


if __name__=="__main__":
    N, M, K = map(int, input().split())  # N개의 카드, M은 같은 카드를 고른다, K번 제출한다

    cards = list(map(int, input().split()))  # 각 카드

    charles = list(map(int, input().split()))  # 철수가 낼 카드

    answer = solution(cards, charles, N, M, K)  # 결과

    for i in answer:  # 결과 출력
        print(i)