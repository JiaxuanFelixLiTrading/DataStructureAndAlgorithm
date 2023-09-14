import sys

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        return
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()
s.push(3)
s.push(2)
s.push(1)
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.pop())
