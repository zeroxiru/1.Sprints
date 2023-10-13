class Stack:

    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return  len(self.items)

    def top(self):
        return self.items[-1]


def reverse_string(string_input):
    s = Stack()
    for i in range(len(string_input)):
        s.push(string_input[i])
    reversed_string = ""
    while not s.is_empty():
        reversed_string = reversed_string + s.pop()
    return reversed_string


def is_palindrome(input_string):
    reversed_string = reverse_string(input_string)
    return input_string == reversed_string

if __name__ == "__main__":
    print(reverse_string("racecar"))
    print(is_palindrome("abba"))