def merge_sort_count(items):
    if len(items) < 2:
        return (items, 0)

    left, left_count = merge_sort_count(items[:len(items) // 2])
    right, right_count = merge_sort_count(items[len(items) // 2:])

    count = left_count + right_count
    result = []
    i = j = 0
    left_len = len(left)
    right_len = len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1

    result.extend(left[i:] + right[j:])
    return (result, count)

