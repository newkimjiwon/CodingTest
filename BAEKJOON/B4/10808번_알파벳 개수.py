words = input()

alpha = {chr(i): 0 for i in range(97, 123)}

for word in words:
    alpha[word] += 1

for i in alpha:
    print(alpha[i], end = ' ')