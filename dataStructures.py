class Queue:
    def __init__(self, *args) -> None:
        self.container = list(args)


    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        index = self.container.index(self.container[0])
        temp = self.container[1:]
        self.container = temp

    def pop(self):
        self.dequeue()

    def is_empty(self):
        if len(self.container) == 0:
            return True
        return False

    def size(self):
        return len(self.container)
    
queue = Queue(1,2,3,4,5,6)
queue.dequeue()
queue.enqueue(7)
print(queue.container)