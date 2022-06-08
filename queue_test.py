class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # リストに追加ではなく、先頭に挿入していることに注意
        # リスト末尾が最古のアイテムとなる
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# TEST
a_queue = Queue()
print(a_queue.is_empty())
print(a_queue.size())
print("----------")

for i in range(0, 5):
    a_queue.enqueue(i * 1000)

print(a_queue.is_empty())
print(a_queue.size())
print("----------")

while a_queue.size():
    print(a_queue.dequeue())

print(a_queue.is_empty())
print(a_queue.size())
print("----------")
