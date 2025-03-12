from random import randint


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


nums = [randint(1, 10**6) for _ in range(10**2)]
print(nums)

sorted_nums = bubble_sort(nums)
print(sorted_nums)
