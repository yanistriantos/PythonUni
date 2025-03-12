# def binary_search(list, objective, start, end ):
#     if start > end:
#         return -1

#     center = (start + end) // 2
#     if list[center] == objeotive:
#         return center
#     elif list[center] < objeotive:
#         return binary_search(list, objective, center + 1, end)
#     else:
#         return binary_search(list, objective, start, center - 1)

# # Example of use
# list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
# objective = 27
# start_search = 0
# end_search = len(list) - 1

# result = binary_search(list, objective_number, start_search, end_search)

# if result != -1:
#     print(f"The number {objective_number} is in position: {result}.")
# else:
#     print(f"The number {objective_number} is NOT in the list")


# iterative version
def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2  # Find the middle index
        if arr[mid] < target:  # If middle element is smaller, search the right half
            start = mid + 1
        elif arr[mid] > target:  # If middle element is larger, search the left half
            end = mid - 1
        else:
            return mid  # If middle element is the target, return its index
    return -1  # If target is not found, return -1
