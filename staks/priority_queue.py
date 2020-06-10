import queue

q = queue.PriorityQueue()
q.put((2, 'I'))
q.put((3, 'You'))
q.put((5, 'we'))

while not q.empty():
    print(q.get())
