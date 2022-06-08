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


