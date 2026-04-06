from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque([])
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        x=self.queue.popleft()
        return x
        

    def top(self) -> int:
        x = self.queue[0]
        return x
        

    def empty(self) -> bool:
        if len(self.queue)>0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()