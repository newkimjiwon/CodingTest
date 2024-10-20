n = int(input())

words = []

for _ in range(n):
    word = input()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key = lambda i:len(i))

for i in words:
    print(i)