import sys

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 1 if len(self.stack) == 0 else 0
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]

# 입력 받기
n = int(sys.stdin.readline().strip())
stack = Stack()

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())