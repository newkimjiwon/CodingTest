if __name__=="__main__":
    n = int(input())
    people = list(map(int, input().split()))
    enough = list(map(int, input().split()))
    
    stamina = [0] * (100)

    for peo, eno in zip(people, enough):
        for i in range(99, peo - 1, -1):
            stamina[i] = max(stamina[i], stamina[i - peo] + eno)
        
    print(max(stamina))