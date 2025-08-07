def solution(n):
    count = 1
    room = 1
    
    while count < n:
        # print(count)
        count += (6 * room)
        room += 1

    # print(count)
        
    return room


if __name__=='__main__':
    n = int(input())
    print(solution(n))