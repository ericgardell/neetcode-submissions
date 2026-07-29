class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None or val < self.min:
            print("\tmin updated to ", val)
            self.min = val
        print("inserting ", val)
        self.stack.append(val)

    def pop(self) -> None:
        # need to handle min now
        val = self.stack.pop()
        print("popping ", val)
        return val

    def top(self) -> int:
        top = self.stack[-1]
        print(f"top is {top}")
        return top

    def getMin(self) -> int:
        print(f"min is {self.min}")
        return min(self.stack)
