def solution(a, arr):
    answer = [-10000000000]

    for i in range(a):
        left = 0
        right = len(answer)

        if answer[-1] < arr[i]:
            answer.append(arr[i])
        else:
            while left < right:
                center = (left + right) // 2
                if answer[center] < arr[i]:
                    left = center + 1
                else:
                    right = center
            answer[right] = arr[i]
    
    print(len(answer) - 1)

def main():
    # 배열 크기
    a = int(input())
    # 배열 
    arr_a = list(map(int, input().split()))

    solution(a, arr_a)

main()