# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"





from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue2.put(value)
    
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
    
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

stack = Stack()
output = []


stack.push(1)
stack.push(2)


output.append(stack.pop())
stack.push(3)
output.append(stack.pop())
output.append(stack.pop())

output_str = ", ".join([str(item) for item in output])
print(output_str)