from collections import deque
import sys
input = sys.stdin.read

def push(q, i):
    q.append(i)

def front(q, result):
    if q:
        result.append(q[0])
    else:
        result.append(-1)

def back(q, result):
    if q:
        result.append(q[-1])
    else:
        result.append(-1)

def size(q, result):
    result.append(len(q))

def empty(q, result):
    result.append(0 if q else 1)

def pop(q, result):
    if q:
        result.append(q.popleft())
    else:
        result.append(-1)

n, *commands = input().splitlines()
n = int(n)

# deque queue
q = deque()
result = []

for command in commands:
    current = command.split()
    if current[0] == 'push':
        push(q, int(current[1]))
    elif current[0] == 'front':
        front(q, result)
    elif current[0] == 'back':
        back(q, result)
    elif current[0] == 'size':
        size(q, result)
    elif current[0] == 'empty':
        empty(q, result)
    elif current[0] == 'pop':
        pop(q, result)

# Join results and print once
sys.stdout.write("\n".join(map(str, result)) + "\n")