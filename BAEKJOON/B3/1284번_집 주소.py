def len(arr):
    answer = 0

    for word in arr:
        if int(word) == 1:
            answer += 2
        elif int(word) == 0:
            answer += 4
        else:
            answer += 3
        answer += 1
    answer += 1
    
    return answer

while True:
    n = list(str(input()))
    if n[0] == '0':
        break
    print(len(n))