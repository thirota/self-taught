
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

    def __repr__(self):
        s = ""
        s = "size: " + str(len(self.items)) + ", item: "
        for item in self.items:
            s += str(item) + ","
        return s




# TEST
stack = Stack()
print(stack.is_empty())
print(stack.size())
print("----------")

stack.push(100)
print(stack.is_empty())
print(stack.size())
print("----------")

item = stack.pop()
print(item)
print(stack.is_empty())
print(stack.size())
print("----------")

for i in range(0, 6):
    stack.push(i * 100)

print(stack.is_empty())
print(stack.size())
print(stack.peek())
print(stack)
print(stack.peek())
print("----------")

item = stack.pop()
print(item)
print(stack.is_empty())
print(stack.size())
print(stack)
print("----------")


charStack = Stack()
for c in "Hello":
    charStack.push(c)

reverse = ""
while charStack.size():
    reverse += charStack.pop()
print(reverse)