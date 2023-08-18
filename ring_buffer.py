from collections import deque

class RingBuffer: 
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.count = 0
        self.size = size

    def add(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        if self.count > self.size:
            self.count = 0
        data = self.data[self.count]
        self.count = self.count + 1
        return data

    def getAll(self):
        return self.data
    