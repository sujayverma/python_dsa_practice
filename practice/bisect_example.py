import heapq
import bisect

# heapq: Binary heap (Priorty Queue) - always keeps the smallest element.
grades = [90, 70, 85]
heapq.heapify(grades) # rearranges a list in-place into a heap

print(grades)
heapq.heappush(grades, 60)
print(grades)

print(heapq.heappop(grades))

# bisect: Binary search for keeping lists sorted.
sorted_nums = [10, 20, 30, 40, 50]

index = bisect.bisect_left(sorted_nums, 25)
print(index)