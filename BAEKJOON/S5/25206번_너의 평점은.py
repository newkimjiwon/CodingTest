def solution():
    score = 0.0
    total = 0.0

    dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
           'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

    for _ in range(20):
        c, t, s = map(str, input().split())
        t = float(t)

        if s == 'P':
            continue

        point = dic[s]
        score += (t * point)
        total += t

    if total == 0.0:
        print(0.000000)
    else:
        print(score / total)


if __name__=="__main__":
    solution()