def linear_search(list, objective):

    for i in range(len(list)):
        if list[i] == objective:
            return i

    return -1


list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
objective_number = 39
result = linear_search(list, objective_number)

if result != -1:
    print(f"The number {objective_number} is located at position: {result}")
else:
    print(f"The number {objective_number} is NOT in the list")

# This algorithm can be useful for traversing small lists or unordered lists
#  but it is not efficient for traversing very long lists.
