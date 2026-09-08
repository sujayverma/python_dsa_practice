from collections import Counter
import heapq


def top_k_frequency(words, k):

    counts = Counter(words)

    print(counts)
    heap = [(-count, word) for word, count in counts.items()]
    print(heap)
    heapq.heapify(heap)
    print(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]

storage = ["apple", "banana", "apple", "cherry", "banana", "apple"]

print(top_k_frequency(storage,3))