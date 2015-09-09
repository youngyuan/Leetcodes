class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.q:
            return
        self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        if not self.q:
            return

        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
while not s.empty():
    print(s.top())
    s.pop()
