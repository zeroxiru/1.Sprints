class Stack:
    def __init__(self):
        self.items =[]

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.is_empty():
            return  self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return  len(self.items)

    def top(self):
        return self.items-1

    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())

