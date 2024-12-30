if __name__ == "__main__":
    dic_color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
                 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    dic_value = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000,
                 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}

    answer = 0

    for i in range(3):
        word = input()
        if i == 0:
            answer += dic_color[word]
        if i == 1:
            answer *= 10
            answer += dic_color[word]
        if i == 2:
            answer *= dic_value[word]

    print(answer)