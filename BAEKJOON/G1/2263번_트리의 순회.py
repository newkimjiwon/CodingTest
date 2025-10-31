import sys
sys.setrecursionlimit(200000)

def solution(N, in_order, post_order):
    answer = []

    in_idx = {}  # in_idx 설정

    for i in range(N):
        in_idx[in_order[i]] = i

    def get_preorder(in_s, in_e, post_s, post_e):
        if in_s > in_e or post_s > post_e:
            return

        root_val = post_order[post_e]
        answer.append(str(root_val))
        
        root_in_idx = in_idx[root_val]
        
        L = root_in_idx - in_s
        
        get_preorder(in_s, root_in_idx - 1, post_s, post_s + L - 1)
        
        get_preorder(root_in_idx + 1, in_e, post_s + L, post_e - 1)

    get_preorder(0, N - 1, 0, N - 1)

    return ' '.join(answer)


if __name__=="__main__":
    N = int(input())  # n개의 정점

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    print(solution(N, in_order, post_order))