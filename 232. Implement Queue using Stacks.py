#232. Implement Queue using Stacks
#https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29

class MyQueue:
    a=[]
    def __init__(self):
        self.a=[]

    def push(self, x: int) -> None:
        self.a.append(x)
        

    def pop(self) -> int:
        b=self.a.pop(0)
        return b
        

    def peek(self) -> int:
        return self.a[0]
        

    def empty(self) -> bool:
        if len(self.a)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()