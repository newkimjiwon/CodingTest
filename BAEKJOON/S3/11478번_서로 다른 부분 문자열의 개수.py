def solution():
    s = list(input())

    result = {}

    for i in range(1, len(s) + 1):
        for ii in range(len(s) - i + 1):
            word = ''.join(s[ii:ii+i])
            if not result.get(word):
                result[word] = 0
            else:
                continue
            
    print(len(result))


if __name__=="__main__":
    solution()