class MinStack:

    def __init__(self):
        self.stack = []

        self.minStack = []

    def push(self, val: int) -> None:
        # print("inserting ", val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

        # print(f"\tminStack now {self.minStack}")
        self.stack.append(val)
        # print(f"\tstack now {self.stack}")
        

    def pop(self) -> None:
        # need to handle min now
        val = self.stack.pop()
        self.minStack.pop()
        # print("popping ", val)
        # print(f"\tminStack now {self.minStack}")
        # print(f"\tstack now {self.stack}")
        return val

    def top(self) -> int:
        top = self.stack[-1]
        # print(f"top is {top}")
        return top

    def getMin(self) -> int:
        # print(f"min:")
        # print(f"\tstack now {self.stack}")
        # print(f"\tminStack is {self.minStack}")
        return self.minStack[-1]
        