
# Question:
# Given an array of integers nums and an integer target, 
# return the indices of the two numbers such that they add up to target.

def find_sum_of_two(arr, target):
    sum = {}

    for i, num in enumerate(arr):

        remains = target - num

        if remains in sum:
            return [sum[remains], i]  # returns the index
            # return [remains, num] # returns the value

        sum[num] = i

    return []


lt = [2,7,8,11,13]
target = 24
# print(find_sum_of_two(lt, target))


def find_sum_with_pointers(srt_arr, target):
    left = 0
    right = len(srt_arr) - 1

    while left < right:
        sum = srt_arr[left] + srt_arr[right]

        if sum == target:
            return [left, right]
        
        elif sum < target:
            left += 1

        else:
            right -= 1

    return []

# sort_array = [1, 2, 3, 4, 6]
# target = 6
# print(find_sum_with_pointers(lt, target))


def find_sum_pair(arr, target):

    seen = set()
    result = set()

    for i,num in enumerate(arr):
        remains = target - num

        if remains in seen:
            pair = min(num,remains), max(num,remains)
            result.add(pair)

        seen.add(num)
        print(f'SEEN: {seen}')
        print(f'RESULT: {result}')

    return result

nums = [1, 2, 3, 4, 3]
target = 6

print(find_sum_pair(nums, target))

