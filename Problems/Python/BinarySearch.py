sorted_data = [2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 25, 65, 77, 89, 98]
target = 25


# Linear Search
def linear_search(data, target):
    for i in len(data):
        if data[i] == target:
            return True
    return False

# Binary Search - iterative
def binary_search(data: list, target: int) -> bool:
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

# Binary Search - recursive
def binary_search_rv(data, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_rv(data, target, start=start, end=mid-1)
        else:
            return binary_search_rv(data, target, start=mid+1, end=end)


# print(binary_search(sorted_data, target))
# print(binary_search_rv(sorted_data, target, 0, len(sorted_data)-1))
