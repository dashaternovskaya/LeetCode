class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.start_pos = 0
        self.end_pos = -1


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end_pos = (self.end_pos + 1) % self.k
        self.queue[self.end_pos] = value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.start_pos] = None
            self.start_pos = (self.start_pos + 1) % self.k
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.start_pos]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.end_pos]


    def isEmpty(self) -> bool:
        return self.queue.count(None) == self.k


    def isFull(self) -> bool:
        return self.queue.count(None) == 0
