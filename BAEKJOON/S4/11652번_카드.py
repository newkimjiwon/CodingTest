if __name__=="__main__":
    n = int(input())

    dic = {}
    s = set()
    max_card = 1

    for _ in range(n):
        card = int(input())

        s.add(card)

        if not dic.get(card):
            dic[card] = 1
        else:
            dic[card] += 1
            if dic[card] > max_card:
                max_card = dic[card]

    s = list(s)
    s.sort()

    for i in s:
        if dic[i] == max_card:
            print(i)
            break