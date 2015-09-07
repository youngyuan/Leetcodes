class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = list()
        self.minstack = list()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minstack.append(x)
        else:
            self.stack.append(x)
            min = self.minstack[-1]
            if x < min:
                self.minstack.append(x)
            else:
                self.minstack.append(min)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.minstack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]


    # @return an integer
    def getMin(self):
        if len(self.minstack) > 0:
            return self.minstack[-1]
        
