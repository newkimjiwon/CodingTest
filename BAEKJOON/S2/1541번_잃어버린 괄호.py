# 수학 식
expressions = input()

math = []
line = ""

for i in range(len(expressions)):
    if expressions[i] == '-':
        math.append(line)
        math.append('-')
        line = ""
        continue
    elif expressions[i] == '+':
        math.append(line)
        math.append('+')
        line = ""
        continue
    if i == len(expressions) - 1:
        line += expressions[i]
        math.append(line)
        break
    line += expressions[i]

answer = 0

end = True

for i in range(len(math)):
    if math[i] == '-':
        end = False
    elif math[i].isdigit():
        if end:
            answer += int(math[i])
        else:
            answer -= int(math[i])
        
print(answer)