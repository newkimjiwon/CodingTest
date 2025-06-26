def main():
    e, s, m = map(int, input().split())

    times = 0  # 정답

    ee, ss, mm = 1, 1, 1

    while (e != ee) or (s != ss) or (m != mm):
        times += 1  # 1년이 지남

        ee += 1
        ss += 1
        mm += 1

        if ee > 15:
            ee = 1
        if ss > 28:
            ss = 1
        if mm > 19:
            mm = 1

    print(times + 1)


if __name__=="__main__":
    main()