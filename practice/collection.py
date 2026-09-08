from collections import Counter, defaultdict, deque

# defaultdict automatically initializes missing keys

counts = defaultdict(int) # default value of new key is zero.
print(counts["apple"])
counts["apple"] += 1
print(counts["apple"])
counts["apple"] += 1
print(counts["apple"])


# Counnter counts the frequeny of an element.
letters = Counter("banana")
print(letters)
print(letters.most_common(2))

# deque: A double ended queue for faster append/pops from both the ends.
queue = deque(["task1", "task2"])
queue.append("task3")
print(queue)
queue.appendleft("task0")
print(queue)
queue.popleft()
print(queue)

