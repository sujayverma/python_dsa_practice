class Stack:
    def __init__(self):
        self.arr = [0] * 5
        self.top = -1

    # Method to push element in.
    def push(self,x):
        if self.top == 4:
            print("Stack Overflow")
            return
        
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        self.top -= 1

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i], end = " ")
        print()



stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)
stack.pop()
print(stack.arr)
stack.display()