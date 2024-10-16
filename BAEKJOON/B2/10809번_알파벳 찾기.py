word = list(str(input()))

idx = {chr(97 + i): -1 for i in range(26)}

for i in range(len(word)):
    if idx[word[i]] == -1:
        idx[word[i]] = i

for i in idx:
    print(idx[i], end = " ")