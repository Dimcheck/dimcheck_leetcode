
def greedy_workers(array: list):
    workers = []
    start = 0
    end = len(array) - 1
    array = sorted(array)

    while start <= end:
        workers.append([array[start], array[end]])
        start += 1
        end -= 1

greedy_workers(array=[6, 3, 2, 7, 5, 5, 8])