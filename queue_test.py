import time
import random

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



def simulate_ticket_line(till_show, max_time):
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue("person" + str(i))
    
    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    
    return tix_sold





# TEST for ticket_line
sold = simulate_ticket_line(5, 1)
print(sold)





# TEST for just Queue
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
