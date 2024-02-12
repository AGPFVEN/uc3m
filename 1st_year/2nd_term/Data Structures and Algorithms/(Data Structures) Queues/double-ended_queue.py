class DoubleEndedQueue:
    def __init__(self):
        self.queue = []

    def addLast(self, e):
        self.queue.append(e)

    def addFirst(self, e):
        self.queue.insert(0, e)

    def removeFirst(self):
        del self.queue[0]

    def removeLast(self, e):
        del self.queue[-1]

    def isEmpty(self):
        if (self.queue.len == 0):
            return True

    def __len__(self):
        return len(self.queue)