# Ryan Lugo: RJl 1/24/22

def flatten_and_sort(array):
    table = []
    for item in array:
        table += item
    return sorted(table)


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6, 100])
print(flatten_and_sort([[], [1]]) == [1])