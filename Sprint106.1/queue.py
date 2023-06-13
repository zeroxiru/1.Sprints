class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        if self.is_empty():
            raise Exception("queueis empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    # Example usage
queue = Queue()

# Enqueue elements
queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("cherry")

# Dequeue an element
item = queue.dequeue()
print("Dequeued item:", item)

# Check the size of the queue
print("Queue size:", queue.size())

# Peek at the front element
front_item = queue.peek()
print("Front item:", front_item)

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())
