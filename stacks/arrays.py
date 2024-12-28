def minimum_swaps(arr):
    lookup = {value: index for (index, value) in enumerate(arr)}
    swaps = 0
    for index in range(len(arr)):
        if arr[index] != index + 1:
            arr[lookup[index + 1]] = arr[index]
            lookup[arr[index]] = lookup[index + 1]
            swaps += 1
    return swaps

# minimum_swaps([4, 3, 1, 2])


def array_manipulation(n, queries):
    items = [0] * (n + 1)
    acc = 0
    result = 0
    for first, last, value in queries:
        items[first - 1] += value
        items[last] -= value

    for value in items:
        acc += value
        result = max(result, acc)
    return result

# array_manipulation(5, [(1, 2, 100), (2, 5, 100), (3, 4, 100)])
