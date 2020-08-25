# implement a queue with its operations, but using stacks -- leetcode
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []

    def push(self, x: int):
        """
        Push element x to the back of queue.
        """
        self.storage.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.storage.pop(0)
        

    def peek(self):
        """
        Get the front element.
        """
        return self.storage[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.storage) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# https://leetcode.com/problems/implement-queue-using-stacks/