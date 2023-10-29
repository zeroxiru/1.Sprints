from exercise_2 import Stack
class Queue:
    def __init__(self):
        self._items = []


    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("Queue is empty")



    def reverse_string(self, word):
        reverse_queue = Queue()
        reverse_string = ""

        for character in word:
            reverse_queue.enqueue(character)

        while not reverse_queue.is_empty():
            reverse_string = reverse_queue.dequeue() + reverse_string
        return reverse_string

    def reverse_stack(self, stack):
        if not stack:
            return stack
        queue = Queue()
        while stack:
            queue.enqueue(stack.pop())

        while not queue.is_empty():
            stack.append(queue.get())

        return stack




    def __str__(self):
        return str(self._items)
if __name__ == "__main__":
    q = Queue()
    # customers_queue = Queue()
    # customers_queue.enqueue("Ibrahim")
    # customers_queue.enqueue("Rumpa")
    # print(customers_queue.size())
    # customers_queue.enqueue("Zohan")
    # customers_queue.enqueue("Mehrish")
    # print(customers_queue)
    # customers_queue.dequeue()
    # print(customers_queue.size())

    word_string = "BOOK"
    print(q.reverse_string(word_string))

    reverse_stack = [1, "hello", "fact", 9]

    stack = [1, "hello", "fact", 9]
    print("Original Stack:", stack)

    reversed_stack = reverse_stack(stack)
    print("Reversed Stack:", reversed_stack)