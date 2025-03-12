from random import randint

nums = sorted([i for i in range(1, 10**3 + 1)])
element = 500


def binary_search(nums, element):
    counter = 0
    low = 0
    high = len(nums) - 1
    while low <= high:
        counter += 1
        mid = (low + high) // 2
        if nums[mid] == element:
            print(counter)
            return mid
        elif nums[mid] < element:  # [1, 3, 5, 7. 9]
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search(nums, element))
